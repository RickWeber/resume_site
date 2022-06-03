from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib import messages
from .forms import GuessForm
from .models import (
    TodaysAnswer,
    Guess,
    Game
)

# Create your views here.

class HomeView(TemplateView):
    template_name='wordle_search/home.html'

    def post(self, request):
        if request.POST.get("Submit"):
            game = Game()
            form = GuessForm()
            previous_guesses = request.POST.get("previous_guesses")
            previous_guesses = previous_guesses.split(" ")
            previous_guesses += request.POST.get("guess")
            for guess in previous_guesses:
                game.make_guess(guess)
            ctx = {'form': form, 'guesses': " ".join(previous_guesses),
            'possible_words': game.show_possible_words(),
            'previous_flags': game.flags}
            return render(request, self.template_name, ctx)

    def get(self, request):
        game = Game()
        form = GuessForm()
        ctx = {'form': form, 
        'possible_words': game.show_possible_words(), 
        'game': game}
        return render(request, self.template_name, ctx)
#
#    def post(self, request):
#        game = request.game
#        form = GuessForm(request.POST)
#        if request.POST.get("guess"):
#            game = Game.objects.last()
#            Game().make_guess(request.POST.get("guess"))
#
#
#        messages.add_message(request, messages.SUCCESS, 'Guess accepted.')
#        return render(request, self.template_name, ctx)
#        #return redirect(reverse('wordle_search:wordle_home'))


class CheatView(DetailView):
    model = TodaysAnswer
    template_name = "wordle_search/cheat.html"
    def get_context_data(self):
        context = super().get_context_data()
        context["answer"] = TodaysAnswer().word
        return context

# TODO:
# * Get the form template together
# * make sure we keep redirecting back
# * have it take input and show the status of the game we've been running.
# * move to a beefier database.