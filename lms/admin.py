from django.contrib import admin

from .models import Author, Book, LibraryBranch, LibraryCard, Patron, Status


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(LibraryBranch)
admin.site.register(LibraryCard)
admin.site.register(Patron)
admin.site.register(Status)
