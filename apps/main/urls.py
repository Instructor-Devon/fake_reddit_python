from django.conf.urls import url
from . import views
urlpatterns = [
    # localhost:8000/
    url(r'^$', views.index),
    # /users/<user_id>
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^like/(?P<post_id>\d+)$', views.like),
    url(r'^posts/(?P<post_id>\d+)$', views.show_post),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^newpost$', views.newpost)
]