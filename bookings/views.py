from django.shortcuts import render
from django.views.generic import DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Booking

class BookingDetailView(DetailView):
    model = Booking
    pk_url_kwarg = "pk"
