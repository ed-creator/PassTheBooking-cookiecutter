from django.conf.urls import url

from passthekeys.users.views import UserDetailView
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^property/(?P<pk>\d+)/$',
        view=views.PropertyDetailView.as_view(),
        name='property_detail'
    ),
    url(
        regex=r'^new_property/$',
        view=views.PropertyCreateView.as_view(),
        name='create_property'
    ),
]
