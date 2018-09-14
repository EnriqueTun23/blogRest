from rest_framework.generics import (ListAPIView, 
RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView,
CreateAPIView)
from blog.models import post
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser,
IsAuthenticatedOrReadOnly)
from .serializers import (PostListSerializer, PostCreateSerializer, 
PostUpdateSerializer,PostDetailSerializer)
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

class PostCreateAPIView(CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class = PostPageNumberPagination

class PostDetailAPIView(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer

    def delete(self, request, pk):
        queryset = get_object_or_404(post, id=pk)
        queryset.delete()


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDestroyAPIView(DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostDetailSerializer
    

