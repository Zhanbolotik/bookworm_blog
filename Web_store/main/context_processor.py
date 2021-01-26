from .models import Category, Review


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def get_books(request):
    books = Review.objects.all()
    return {'books': books}