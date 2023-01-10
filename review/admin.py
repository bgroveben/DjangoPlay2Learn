from django.contrib import admin

from .models import Game
from .models import Review


admin.site.register(Game)
admin.site.register(Review)
