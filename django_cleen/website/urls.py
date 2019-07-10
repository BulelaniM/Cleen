from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cleen-home-page'),
    path('home/', views.home, name='cleen-home'),
    path('about/', views.about, name='cleen-about'),
    path('book/', views.book_cleen, name='cleen-book'),
    path('join/', views.join_cleen, name='cleen-join'),
    path('help/', views.help_cleen, name='cleen-help'),
]