from .models import Products,Users
from .forms import UserRegisterForm
from django.views.generic import ListView,CreateView


class HomeView(ListView):
    model = Products
    template_name = 'product.html'
    context_object_name = 'products'


class RegisterView(CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = 'login'


class LoginView(CreateView):
    next_page = '/'
    model = Users
    redirect_authenticated_user = False
    template_name = 'login.html'
    success_url = 'register'
