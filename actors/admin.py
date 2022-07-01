from django.contrib import admin
from .models import Actor
from datetime import date
# Register your models here.
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    # fields=('name','gender','dob','profile_picture')
    search_fields=('name','gender')
    list_filter=('gender',)
    list_display =('name','gender','profile_picture','movie_count','age')
    fieldsets = (
      ('Standard info', {
          'fields': ('name',)
      }),
      ('Personal info', {
          'fields': ('dob', 'gender', 'profile_picture')
      }),
      
   )

    def movie_count(self, obj):
        return obj.movie_set.count()

    def age(self,obj):
            today = date.today()
            age=today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))
            return str(age)
