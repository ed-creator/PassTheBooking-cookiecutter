from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^bookings/(?P<pk>\d+)/$',
        view=views.BookingDetailView.as_view(),
        name='booking_detail'
    ),
]
