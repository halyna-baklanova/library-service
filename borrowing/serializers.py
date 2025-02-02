from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ["id", "user", "book", "book_title", "book_author"]
        read_only_fields = ["user", "borrowed_at", "returned_at"]

    def validate(self, data):
        if data["book"].inventory == 0:
            raise ValidationError("This book is out of stock.")
        return data

    def create(self, validated_data):
        book = validated_data["book"]
        book.inventory -= 1
        book.save()
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
