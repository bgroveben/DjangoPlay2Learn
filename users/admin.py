from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

from common.admin import DjangoPlay2LearnAdmin
from common.utils.admin import append_fields, move_fields, remove_fields

from .models import CustomUser, ReviewModel, ReviewVote

#CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(DjangoPlay2LearnAdmin, UserAdmin):
    model = CustomUser

    # List Attributes
    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    # Read-only Fields
    readonly_fields = ['password_form']

    # Fields for editing existing user.
    new_fields = ('dob', 'avatar')
    # Add new fields to 'Personal info' fieldset.
    append_fields(UserAdmin.fieldsets, 'Personal info', new_fields)
    # Move email field from 'Personal info' fieldset to unlabelled fieldset
    move_fields(UserAdmin.fieldsets, 'Personal info', None, ('email',))
    # Remove password field.
    remove_fields(UserAdmin.fieldsets, None, ('password',))
    append_fields(UserAdmin.fieldsets, None, ('password_form',))

    # Fields for adding new user.
    new_fields = ('email', )
    # Add new fields to unlabelled fieldset.
    append_fields(UserAdmin.add_fieldsets, None, new_fields)

    # Add optional fields to new 'Optional Fields' fieldset.
    optional_fields = ('first_name', 'last_name', 'dob')
    add_fieldsets = append_fields(
        UserAdmin.add_fieldsets, 'Optional Fields', optional_fields
    )

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    # Add Save buttons to the top of the change user form
    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)

@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    model = ReviewModel
    #list_display = ['vote', 'comment', 'game', 'customuser', 'created', 'updated']
    list_display = ['comment', 'game', 'customuser', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()


@admin.register(ReviewVote)
class ReviewVoteAdmin(admin.ModelAdmin):
    model = ReviewVote
    list_display = ['review', 'customuser', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')
        return ()



admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)


"""
https://blog.devgenius.io/lets-build-a-movie-review-django-app-47658f8e3751

from django.contrib import admin

from . models import Movie
from . models import Review


admin.site.register(Movie)
admin.site.register(Review)
"""
