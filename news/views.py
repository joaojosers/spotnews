from django.shortcuts import render, redirect
from .models import News, Category
from .forms import FormCategories, FormNews


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

    return render(
        request,
        "categories_form.html",
        {"form": form, "show_categories_link": True}
    )


def news_form(request):
    form = FormNews()
    if request.method == "POST":
        form = FormNews(request.POST, request.FILES)
        if form.is_valid():
            # Salvando os dados do formulário no modelo News
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            created_at = form.cleaned_data['created_at']
            image = form.cleaned_data['image']
            categories = form.cleaned_data['categories']
            news = News.objects.create(
                title=title,
                content=content,
                author=author,
                created_at=created_at,
                image=image)
            news.categories.set(categories)
            return redirect("home-page")
    return render(
        request,
        "news_form.html",
        {"form": form, "categories": Category.objects.all()},
    )
