from django.contrib.auth.forms import UserCreationForm

from .models import Users



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'staff', 'email', 'password1']