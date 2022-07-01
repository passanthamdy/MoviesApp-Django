from django.contrib import admin

from .models import Movie, Director

class MovieAdminInline(admin.TabularInline):
        extra = 1
        model = Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
   fields=('name','production_year','image','director')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    inlines=(MovieAdminInline,)
    fields = ('name',) 
    search_fields=('movie__name',)




