from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Property

class PropertyDetailView(DetailView):
    model = Property
    pk_url_kwarg = "pk"


class PropertyListView(ListView):
    model = Property

    slug_field = 'address'
    slug_url_kwarg = 'address'

class PropertyUpdateView(UpdateView):
    model = Property

    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

class PropertyCreateView(CreateView):
    model = Property
    fields = ['address_line_one','address','no_of_bedroom','sq_feet']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PropertyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:property:detail',
                       kwargs={'username': self.request.user.username})
