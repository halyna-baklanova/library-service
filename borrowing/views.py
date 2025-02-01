from django.db import models
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Borrowing
from .serializers import BorrowingSerializer
from rest_framework.permissions import IsAuthenticated


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["borrowed_at", "returned_at"]

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        if not user.is_staff:
            queryset = queryset.filter(user=user)

        is_active = self.request.query_params.get("is_active")
        if is_active is not None:
            queryset = queryset.filter(
                returned_at__isnull=(is_active.lower() == "true")
            )

        if user.is_staff:
            user_id = self.request.query_params.get("user_id")
            if user_id:
                queryset = queryset.filter(user_id=user_id)

        return queryset

    @action(detail=True, methods=["post"])
    def return_borrowing(self, request, pk=None):
        borrowing = self.get_object()
        if borrowing.returned_at is not None:
            return Response(
                {"error": "This book has already been returned."}, status=400
            )

        borrowing.returned_at = models.DateTimeField(auto_now=True)
        borrowing.save()
        borrowing.book.inventory += 1
        borrowing.book.save()
        return Response({"message": "Book returned successfully."})
