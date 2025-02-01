from rest_framework import viewsets
from .models import Borrowing
from .serializers import BorrowingSerializer
from rest_framework.permissions import IsAuthenticated


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [IsAuthenticated]
