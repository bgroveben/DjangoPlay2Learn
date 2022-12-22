from django.contrib import admin

admin.site.index_title = 'Admin Home'
admin.site.site_title = 'Django Play2Learn Admin'
admin.site.site_header = 'Django Play2Learn Admin'

class DjangoPlay2LearnAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_max_show_all = 1000

    save_as = True
