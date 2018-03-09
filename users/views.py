from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
# from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


# Create your views here.


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
