from django import templates
from App_Keyword.models import Bookmark

register = templates.Library()

@register.filter
def bookmark_list(user):
    bookmark = Bookmark.objects.filter(user=user)

    if bookmark.exists():
        context = {'bookmark': bookmark}
        return context
    else:
        context = {}
        return context