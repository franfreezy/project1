from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='home'), 
    path('blog/', views.blog, name='blogpage'),
    path('homeauto/', views.homeauto, name='homeautopage'),
    path('docs/', views.docs, name='docspage'),
    path('portfolio/', views.portfolio, name='portfoliopage'),

 ]