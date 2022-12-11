from django.urls import path

from games.views import HomeView, GamesView, record_score

app_name = 'games'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('games/', GamesView.as_view(), name='games'),
    path('record-score/', record_score, name="record-score"),
]
