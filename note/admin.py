from django.contrib import admin
from .models import Note

# Register your models here.
class NoteAdmin(admin.ModelAdmin):

    list_display = ['title','created_at']
    list_display_links = ['created_at']
    list_filter = ['created_at']
    search_fields = ['title','content']


    class Meta:
        model = Note


admin.site.register(Note, NoteAdmin)