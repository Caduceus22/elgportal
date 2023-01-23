from django.http import Http404
from django.template.defaulttags import url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tkp_new


def about(request):
    return render(request, 'about.html')


class HomePageView(LoginRequiredMixin, ListView):

    model = Tkp_new
    template_name = 'home.html'
    context_object_name = 'all_tkp_list'


class MyListView(LoginRequiredMixin, ListView):
    template_name = 'mylist.html'
    context_object_name = 'my_list'

    def get_queryset(self):
        return Tkp_new.objects.filter(author=self.request.user)


class TkpDetailView(DetailView):
    model = Tkp_new
    template_name = 'tkp_detail.html'
    context_object_name = 'tkp_detail'


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
              'tender_tkp',
              'notes_tkp',
              ]
    success_url = reverse_lazy('my_list')


class TkpUpdateView(UpdateView):
    model = Tkp_new
    template_name = 'tkp_new_update_form.html'
    fields = ['title',
              'summa_tkp',
              'kontakt_tkp',
              'city_client',
              'description_tkp',
              'tender_tkp',
              'notes_tkp',
              'slug'
              ]
    template_name_suffix = '_update_form'


class TkpDeleteView(DeleteView):
    model = Tkp_new
    template_name = 'tkp_delete.html'
    success_url = reverse_lazy('home')
