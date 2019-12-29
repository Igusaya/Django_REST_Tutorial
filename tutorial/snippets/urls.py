from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include

from snippets.views import UserViewSet
from rest_framework import renderers


user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        user_list,
        name='user-list'),
    path('users/<int:pk>/',
        user_detail,
        name='user-detail'),
    path('api-auth/',
        include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
