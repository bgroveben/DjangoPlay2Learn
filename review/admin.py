from django.contrib import admin

from .models import Review, ReviewModel

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    model = ReviewModel
    #list_display = ['vote', 'comment', 'game', 'customuser', 'created', 'updated']
    list_display = ['comment', 'game', 'customuser', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

admin.site.register(Review)
