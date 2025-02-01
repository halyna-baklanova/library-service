from django.db import models

from book_service.models import Book
from user.models import User


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="borrowing_book"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="borrowing_user"
    )

    @property
    def is_active(self):
        return self.actual_return_date is None

    def __str__(self):
        return f"Borrowing: {self.book} by User: {self.user}"
