from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[MinLengthValidator(2)]
        )
    content = models.TextField(validators=[MinLengthValidator(1)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.title and len(self.title.split()) < 2:
            raise ValidationError(
                {"title": [_("O título deve conter pelo menos 2 palavras.")]}
            )
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     # teste para novo commit
    #     if self.title and len(self.title.split()) < 2:
    #         raise ValidationError(
    #             _("O título deve conter pelo menos 2 palavras.")
    #             )
    #     super().save(*args, **kwargs)
