from django.contrib import admin
from movies.models import Movies

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movies, MoviesAdmin)
