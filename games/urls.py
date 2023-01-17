from django.urls import path

from games.views import HomeView, GamesView, GameScoresView, record_score, MyScoresView

app_name = 'games'
urlpatterns = [
    # send reviews to homepage
    path('', HomeView.as_view(), name='homepage'),
    path('games/', GamesView.as_view(), name='games'),
    path('game-scores/', GameScoresView.as_view(), name='game-scores'),
    path('myscores/', MyScoresView.as_view(), name='myscores'),
    path('record-score/', record_score, name="record-score"),
    #path('myscores/', record_score, name="myscores"),
]
