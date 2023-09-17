from django.views.generic import ListView, DetailView, CreateView

from .models import advertise
# Create your views here.


class Home(ListView):
    model = advertise
    template_name = 'pages/index.html'
    context_object_name = 'elon'


class Detail(DetailView):
    model = advertise
    template_name = 'pages/ok.html'
    context_object_name = 'advertise'


class Post(CreateView):
    model = advertise
    fields = ['product_name', 'description', 'img', 'price', 'location', 'phone_number']
    template_name = 'pages/posts.html'
    success_url = '/'


class Quron(DetailView):
    model = advertise
    template_name = 'pages/quron.html'
    context_object_name = 'advertise'
