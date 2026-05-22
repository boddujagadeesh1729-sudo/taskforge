from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from notifications.tasks import send_task_notification_email

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "priority",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "due_date",
    ]

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user,
        )

    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)

        send_task_notification_email.delay(
            self.request.user.email,
            task.title,
        )
