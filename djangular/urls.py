from django.conf.urls import patterns, url
from .views import DjangularModuleTemplateView

urlpatterns = [
    url(r'^app.js$', DjangularModuleTemplateView.as_view(), name='djangular-module')
]
