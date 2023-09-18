from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ad, salomatlik, kitoblar, quron, offis, ibodat, sovga, parfyum, gozallik
# Create your views here.


class Home(ListView):
    model = ad
    template_name = 'pages/index.html'
    context_object_name = 'ad'


class Detail(DetailView):
    model = ad
    template_name = 'pages/detail.html'
    context_object_name = 'ad'
# Categories


class Salomatlik(ListView):
    model = salomatlik
    template_name = 'pages/salomatlik.html'
    context_object_name = 'salomatlik'

# rahmatjon
class Post(LoginRequiredMixin, CreateView):
    model = ad
    fields = ['product_img', 'product_name', 'description', 'price', 'location', 'phone_number']
    template_name = 'pages/posts.html'
    success_url = '/'
    login_url = 'login'


class Kitoblar(ListView):
    model = kitoblar
    template_name = 'pages/kitoblar.html'
    context_object_name = 'kitoblar'


class Quron(ListView):
    model = quron
    template_name = 'pages/quron.html'
    context_object_name = 'quron'


class UyOffis(ListView):
    model = offis
    template_name = 'pages/offis.html'
    context_object_name = 'offis'


class Ibodat(ListView):
    model = ibodat
    template_name = 'pages/ibodat.html'
    context_object_name = 'ibodat'


class Sovga(ListView):
    model = sovga
    template_name = 'pages/sovga.html'
    context_object_name = 'sovga'


class Parfyum(ListView):
    model = parfyum
    template_name = 'pages/parfyum.html'
    context_object_name = 'parfyum'


class Gozallik(ListView):
    model = gozallik
    template_name = 'pages/gozallik.html'
    context_object_name = 'gozallik'


# DetailView
class SalomatlikDetail(DetailView):
    model = salomatlik
    template_name = 'pages/salomatlikdetail.html'
    context_object_name = 'salomatlik'

