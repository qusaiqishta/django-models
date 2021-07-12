from django.shortcuts import render
from django.views.generic import  ListView, DetailView ,TemplateView
from .models import Snack


class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack


class SnackDetailView(DetailView):
    template_name="snack_details.html"
    model=Snack

class HomeView(TemplateView):
    template_name='base.html'    

# Create your views here.
