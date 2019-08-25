from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^salesaccounttrimesters/$', views.get_data, name="salesaccounttrimesters"),
    # url(r'^$', views.show_data, name='show_data'),
    # url(r'^cuenta/(?P<pk>\d+)$', views.CuentaDetailView.as_view(), name='cuenta-detail'),
    url(r'^salesaccounttrimesters/$', views.SalesAccountTrimesterListView.as_view(), name='salesaccounttrimesters'),
]
