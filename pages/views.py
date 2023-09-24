from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import products, Category
from .forms import PostForm

# Create your views here.


class Home(ListView):
    model = products
    template_name = 'pages/index.html'
    context_object_name = 'item'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    category_post = products.objects.filter(category=cats)
    return render(request, 'pages/category.html', {'cats': cats, 'category_post': category_post})


class Detail(DetailView):
    model = products
    template_name = 'pages/detail.html'
    context_object_name = 'item'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Detail, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class Post(LoginRequiredMixin, CreateView):
    model = products
    form_class = PostForm
    # fields = ['product_img', 'product_name', 'description', 'category', 'price', 'location', 'phone_number']
    template_name = 'pages/posts.html'
    success_url = '/'
    login_url = 'login'


def SearchViews(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        item = products.objects.filter(product_name__contains=searched)
        return render(request, 'pages/search.html', {'searched': searched, 'item': item})
    else:
        return render(request, 'pages/search.html')
