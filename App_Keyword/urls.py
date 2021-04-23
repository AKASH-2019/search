from django.urls import path
from App_Keyword import views
app_name = 'App_Keyword'



urlpatterns = [
    path('', views.keyword, name='home'),
    path('key-site/', views.site, name='site'),
    path('key-demo/<pk>/', views.demo, name='demo'),
    path('key-history/', views.history, name='history'),
    path('key-bookmark/', views.bookmarkList, name='bookmarked'),
    path('bookmark/<pk>/', views.bookmarked, name='bookmark'),
    path('u-bookmark/<pk>/', views.bookmarkCancel, name='u-bookmark'),

]