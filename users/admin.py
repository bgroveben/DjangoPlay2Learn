from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

from common.admin import DjangoPlay2LearnAdmin
from common.utils.admin import append_fields

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(DjangoPlay2LearnAdmin, UserAdmin):
    model = CustomUser

    # List Attributes
    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')
    # Read-only Fields
    readonly_fields = ['password_form']
    # Fields for adding new user.
    new_fields = ('email', )
    # Add new fields to unlabelled fieldset.
    append_fields(UserAdmin.add_fieldsets, None, new_fields)

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    # Add Save buttons to the top of the change user form
    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)


admin.site.unregister(SocialApp)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialToken)
