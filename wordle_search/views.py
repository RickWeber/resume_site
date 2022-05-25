from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import GuessForm
from .models import (
    TodaysAnswer,
    Guess,
    Game
)

# Create your views here.

class HomeView(TemplateView):
    template_name='wordle/home.html'
    def get(self, request):
        form = GuessForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = GuessForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        messages.add_message(request, messages.SUCCESS, 'Guess accepted.')
        return render(request, self.template_name, ctx)
        #return redirect(reverse('wordle_search:wordle_home'))


# TODO:
# * Get the form template together
# * make sure we keep redirecting back
# * have it take input and show the status of the game we've been running.
# * move to a beefier database.