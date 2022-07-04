from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # 이외 메소드는 작성자만 가능하다.
        return obj.author == request.user