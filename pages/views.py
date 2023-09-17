from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ad
# Create your views here.


class Home(ListView):
    model = ad
    template_name = 'pages/index.html'
    context_object_name = 'ad'


class Detail(DetailView):
    model = ad
    template_name = 'pages/detail.html'
    context_object_name = 'ad'


class Post(LoginRequiredMixin, CreateView):
    model = ad
    fields = ['product_img', 'product_name', 'description', 'price', 'location', 'phone_number']
    template_name = 'pages/posts.html'
    success_url = '/'
    login_url = 'login'
