from django.urls import path

from games.views import HomeView, GamesView, GameScoresView, record_score, MyScoresView

app_name = 'games'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('games/', GamesView.as_view(), name='games'),
    path('game-scores/', GameScoresView.as_view(), name='game-scores'),
    path('myscores/', MyScoresView.as_view(), name='myscores'),
    # unauthenticated users who visit /myscores/ will only see
    # My Scores heading followed by blank screen
    path('record-score/', record_score, name="record-score"),
]
