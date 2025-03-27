from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour n'autoriser que les propriétaires à modifier un objet
    """
    def has_object_permission(self, request, view, obj):
        # Les méthodes de lecture sont toujours autorisées
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # N'autoriser que le propriétaire à modifier
        return obj.user == request.user