from django.urls import path
from blog.views import *
from django.urls import include
from blog.feeds import LatestEntriesFeed
app_name = 'blog'

urlpatterns = [
    path('', blog_view,name='index'),
    path('author/<str:author_username>',blog_view,name='author_un'),
    path('tag/<str:tag_name>', blog_view,name='tag'),
    path('test', test, name = 'test'),
    path('<int:pid>', blog_single,name='single'),
    path('search/',blog_search,name='search'),
    path('category/<str:cat_name>', blog_cat,name='cat'),
    path('rss/feed/', LatestEntriesFeed())
]