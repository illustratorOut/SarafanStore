from django.urls import path

from store.apps import StoreConfig
from store.views import view_home

app_name = StoreConfig.name

urlpatterns = [
    path('', view_home, name='home'),

]
