from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class Login(LoginView):
    template_name = 'users/login.html'
    next_page = '/'


class Logout(LogoutView):
    next_page = 'login'
