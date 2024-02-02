from django.urls import path

from src.menu.views import IndexView

app_name = 'menu'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]