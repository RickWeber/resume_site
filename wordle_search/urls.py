from django.urls import path
from . import views

app_name='wordle_search'
urlpatterns = [
    path('', views.HomeView.as_view(), name="wordle_home"),
    path('cheat', views.CheatView.as_view(), name="cheat"),
#    path('word/<int:pk>', views.DayView.as_view(), name="wordle_day"),
]
