import pathlib
import uuid

from django.db import models
from django.utils.text import slugify


def book_cover_path(instance: "Book", filename: str) -> pathlib.Path:
    extension = pathlib.Path(filename).suffix
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}" + extension
    return pathlib.Path("uploads/actors/") / pathlib.Path(filename)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=book_cover_path, null=True, blank=True)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
