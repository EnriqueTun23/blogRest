from django.urls import path
from .views import (PostListAPIView, 
PostDetailAPIView, PostUpdateAPIView, PostDestroyAPIView,
PostCreateAPIView)


urlpatterns = [
    path('',PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view(), name="detail"),
    path('create/', PostCreateAPIView.as_view(),name="create"),
    path('<int:pk>/edit', PostUpdateAPIView.as_view() ),
    path('<int:pk>/delete', PostDestroyAPIView.as_view())
]