from django.urls import path
from . import  views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.post_list, name="index"),
    path('create/', views.post_create),
    path('<int:id>', views.post_detail, name="detail"),
    path('<int:id>/edit', views.post_update, name="update"),
    path('<int:id>/delete', views.post_delete, name="delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
