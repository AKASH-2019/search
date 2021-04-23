from datetime import datetime, timedelta
from pyexpat.errors import messages

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse



# messages
from django.contrib import messages

# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# models
from App_Keyword.models import Keyword, KeywordSearch, Bookmark
from App_Login.models import User

from App_Keyword.forms import TimeDurationForm

@login_required()
def keyword(request):
    startdate = datetime.today()
    enddate30 = startdate - timedelta(days=29)
    # search_home = KeywordSearch.objects.filter(date__range=[enddate30, startdate], user=request.user)
    search_home = KeywordSearch.objects.filter(date__range=[enddate30, startdate], user=request.user)

    # search_home = list(search_home)
    home_card = []
    home_card_pk = []
    for v in search_home:
        if v.page.name in home_card:
            continue
        else:
            home_card.append(v.page.name)
            home_card_pk.append(v.page.pk)

    home_all = zip(home_card[0:4], home_card_pk[0:4])
    # print(home_all)
    # for a,b in home_all:
    #     print(a,b)


    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Keyword.objects.filter(name__icontains=search)

        all_key = Keyword.objects.all()
        if len(search) == 0:
            return render(request, 'App_Keyword/home.html', context={'home_card': home_card, 'home_card_pk':home_card_pk, 'home_all':home_all,})

        if result:
             return render(request, 'App_Keyword/suggestion.html', context={'all_key': all_key, 'search':search, 'result':result,'home_card': home_card,'home_card_pk':home_card_pk, 'home_all':home_all,})
        else:
            messages.warning(request, "page is not found")
            return render(request, 'App_Keyword/home.html', context={'home_card': home_card,'home_card_pk':home_card_pk, 'home_all':home_all,})

@login_required()
def demo(request,pk):
    page = Keyword.objects.get(pk=pk)
    page.count = page.count + 1
    page.save()

    search_key = KeywordSearch(page=page, user=request.user)
    search_key.save()

    bookmark_page = Bookmark.objects.filter(page=page, user=request.user)

    # print(search_key)
    # if user==request.user:
    #     return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Keyword/demo.html', context={'page':page, 'bookmark_page': bookmark_page, })

@login_required()
def history(request):
    form = TimeDurationForm()

    if request.method == "POST":
        form = TimeDurationForm(data=request.POST)
        if form.is_valid():
            start = form.cleaned_data.get('start')
            end = form.cleaned_data.get('end')

            search_history = KeywordSearch.objects.filter(date__range=[start, end], user=request.user)
            context={
                'form': form, 
                'search_history': search_history,
                'start': start,
                'end': end }
            return render(request, 'App_Keyword/duration.html', context)

    else:
        startdate = datetime.today()
        enddate2 = startdate - timedelta(days=2)
        search_history2 = KeywordSearch.objects.filter(date__range=[enddate2, startdate], user=request.user)
        enddate7 = startdate - timedelta(days=6)
        search_history7 = KeywordSearch.objects.filter(date__range=[enddate7, startdate], user=request.user)
        enddate30 = startdate - timedelta(days=29)
        search_history30 = KeywordSearch.objects.filter(date__range=[enddate30, startdate], user=request.user)
        return render(request, 'App_Keyword/history.html', context={'search_history2': search_history2,
                                                                    'search_history7': search_history7,
                                                                    'search_history30': search_history30,
                                                                    'form': form})
    return render(request, 'App_Keyword/history.html', context={'form': form})


@login_required()
def site(request):

    key = Keyword.objects.all()
    user = User.objects.all()

    return render(request, 'App_Keyword/site.html', context={'key':key, 'user':user})
@login_required
def bookmarkList(request):
    bookmark = Bookmark.objects.filter(user=request.user)

    # return render(request, 'App_Keyword/bookmark.html', context={'bookmark':bookmark,})
    return render(request, 'App_Keyword/bookmark.html', context={'bookmark':bookmark,})

@login_required
def bookmarked(request, pk):
    page = Keyword.objects.get(pk=pk)
    page.count = page.count - 1
    page.save()
    already_book = Bookmark.objects.filter(page=page, user=request.user)
    if not already_book:
        bookmark_page = Bookmark(page=page, user=request.user)
        bookmark_page.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     #  redirect to same page

@login_required
def bookmarkCancel(request, pk):
    page = Keyword.objects.get(pk=pk)
    page.count = page.count - 1
    page.save()
    already_book = Bookmark.objects.filter(page=page, user=request.user)
    already_book.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   #  redirect to same page