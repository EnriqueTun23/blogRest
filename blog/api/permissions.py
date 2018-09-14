from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Hola lamento informarle que no tiene permiso para poder editar este articulo"
    def has_object_permission(self, request, view, obj):
            return obj.user == request.user