from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def validate_title(value):
    if not len(str(value).split()) > 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_title],
        blank=False,
        )
    content = models.TextField(
        validators=[MinLengthValidator(1)],
        blank=False
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if self.title and len(self.title.split()) < 2:
    #         raise ValidationError(
    #             {"title": [_("O título deve conter pelo menos 2 palavras.")]}
    #         )
    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # teste para novo commit
    #     if self.title and len(self.title.split()) < 2:
    #         raise ValidationError(
    #             _("O título deve conter pelo menos 2 palavras.")
    #             )
    #     super().save(*args, **kwargs)
