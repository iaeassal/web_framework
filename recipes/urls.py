from django.urls import path
from recipes.views import contato, sobre, home



urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]