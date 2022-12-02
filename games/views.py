from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"
