from django.http import Http404
from django.template.defaulttags import url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tkp_new


class HomePageView(LoginRequiredMixin, ListView):

    model = Tkp_new
    template_name = 'home.html'
    context_object_name = 'all_tkp_list'
    ordering = ['-id']
    paginate_by = 15


class MyListView(LoginRequiredMixin, ListView):
    template_name = 'mylist.html'
    context_object_name = 'my_list'
    paginate_by = 15

    def get_queryset(self):
        return Tkp_new.objects.filter(author=self.request.user).order_by('-id')



class TkpCreateView(LoginRequiredMixin, CreateView):
    model = Tkp_new
    template_name = 'tkp_new.html'
    fields = ['author',
              'title',
              'data_create_tkp',
              'summa_tkp',
              'kontakt_tkp',
              'kontakt_tel',
              'city_client',
              'description_tkp',
              'tkpdf',
              'tender_tkp',
              'notes_tkp',
              ]
    success_url = reverse_lazy('my_list')

