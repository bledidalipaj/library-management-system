from django.contrib import admin

from .models import LibraryBranch, LibraryCard, Patron


admin.site.register(LibraryBranch)
admin.site.register(LibraryCard)
admin.site.register(Patron)
