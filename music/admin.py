from django.contrib import admin
from music.models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Books)
