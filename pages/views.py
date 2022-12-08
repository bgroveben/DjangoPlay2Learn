from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = 'Assignment'
        context['url'] = 'https://www.webucator.com/project/play2learn-complete-website/'

        return context

class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class GamesView(TemplateView):
    template_name = 'pages/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anagramhunt'] = "anagramhunt"
        context['mathfacts'] = "mathfacts"

        return context
