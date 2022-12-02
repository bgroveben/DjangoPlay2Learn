from django.urls import path

from games.views import HomeView, MathFactsView, AnagramHuntView

app_name = 'games'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
]
