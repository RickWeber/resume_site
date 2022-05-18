from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="resume_home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('p/<int:pk>', views.PortfolioView.as_view(), name="portfolio"),
]
