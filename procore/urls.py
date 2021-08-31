from django.urls import path
from .views import (
PostListView,
PostDetailView,
PostCreateView,
PostUpdateView, # new
)

urlpatterns = [
    path('post/<int:pk>/edit/',
        PostUpdateView.as_view(), name='post_update'), # new
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='home'),
]
