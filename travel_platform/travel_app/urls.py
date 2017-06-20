from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coord/', views.coord, name='coord'),
    url(r'^search', views.get_city_tourist_info, name='search_city'),
    url(r'^museum_detail/(?P<id_>[^/]+)/(?P<lang>[a-zA-z]+)/$',
        views.museum_detail, name='museum_detail'),
    url(r'^tour_detail/(?P<id_>[^/]+)/(?P<lang>[a-zA-z]+)/$',
        views.tour_detail, name='tour_detail')
]
