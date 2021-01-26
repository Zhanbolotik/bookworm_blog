from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import NewForm, ImageForm
from .models import *

class MainPageView(ListView):
    model = Review
    template_name = 'index.html'
    context_object_name = 'reviews'
    paginate_by = 2
    def get_template_names(self):
        template_name = super(MainPageView, self).get_template_names()
        search = self.request.GET.get('q')
        if search:
            template_name = 'search.html'
        return template_name
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        if search:
            context['reviews'] = Review.objects.filter(Q(title__icontains=search)|
                                                           Q(description__icontains=search))
        else:
            context['reviews'] = Review.objects.all()
        return context

def category_page(request,slug):
    category = Category.objects.get(slug = slug)
    reviews1 = Review.objects.filter(category = slug)
    return render(request, 'category-page.html', locals())

def book_detail(request, pk):
    book_review = get_object_or_404(Review, pk=pk)
    book = Review.objects.get(pk=pk)
    return render(request, 'book_review.html',locals())

@login_required(login_url='login')
def add_review(request):
    ImageFormSet = modelformset_factory(Image, form= ImageForm, max_num=2)
    if request.method == 'POST':
        review_form = NewForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset = Image.objects.none())
        if review_form.is_valid() and formset.is_valid() :
            new = review_form.save(commit=False)
            new.user = request.user
            new.save()

            for form in formset.cleaned_data:
                image= form['image']
                Image.objects.create(image = image, review = new)
            return redirect('home')
    else:
        formset = ImageFormSet(queryset = Image.objects.none())
        review_form = NewForm()
    return render(request, 'add-review.html', locals())



