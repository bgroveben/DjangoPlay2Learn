from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.index_title = 'Admin Home'
admin.site.site_title = 'Django Djokes Admin'
admin.site.site_header = 'Django Djokes Admin'


class DjangoJokesAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 1000

    save_as = True


CustomUser = get_user_model()
@admin.register(CustomUser)
class CustomUserAdmin(DjangoJokesAdmin, UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Optional Fields', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
