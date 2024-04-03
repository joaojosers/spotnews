from django.shortcuts import render, redirect
from .models import News, Category
from .forms import FormCategories

# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    return render(request, "news_details.html", context)


def categories_form(request):
    form = FormCategories()
    if request.method == "POST":
        form = FormCategories(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    return render(request, "categories_form.html", {"form": form})