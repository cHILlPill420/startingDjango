from django.conf.urls import url
from first_app import views

#for template tagging
app_name = 'first_app'

urlpatterns = [
    url('^datab/$', views.dbdb, name = 'dbdb'),
    url(r'^formpage/$', views.form_view, name = 'formm'),
    url(r'^relative/$', views.relative, name = 'relative'),
]