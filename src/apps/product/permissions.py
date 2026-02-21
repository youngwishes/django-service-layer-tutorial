from rest_framework.permissions import BasePermission


class CustomerRequired(BasePermission):
    def has_permission(self, request, view) -> bool:
        return getattr(request.user, "customer", None)
