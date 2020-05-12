from django.contrib import admin

from .models import (
    Author,
    Book,
    Checkout,
    CheckoutHistory,
    Hold,
    LibraryBranch,
    LibraryCard,
    Patron,
    Status
)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'status', 'location',)
    list_editable = ('status',)
    list_filter = ('status', 'location')
    search_fields = ('title',)


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('pk', 'library_asset', 'library_card', 'since', 'until',)
    search_fields = ('library_asset__title',)


class CheckoutHistoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'library_asset', 'library_card',
                    'checked_out', 'checked_in',)
    search_fields = ('library_asset__title',)


class HoldAdmin(admin.ModelAdmin):
    list_display = ('pk', 'library_asset', 'library_card', 'hold_placed',)
    search_fields = ('library_asset__title',)


class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'address', 'telephone', 'open_date',)


class LibraryCardAdmin(admin.ModelAdmin):
    list_display = ('pk', 'patron', 'fees', 'created',)
    search_fields = ('patron__first_name', 'patron__last_name',)


class PatronAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name',
                    'date_of_birth', 'gender', 'home_library_branch',)
    list_filter = ('gender', 'home_library_branch__branch_name',)

    search_fields = ('first_name', 'last_name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Checkout, CheckoutAdmin)
admin.site.register(CheckoutHistory, CheckoutHistoryAdmin)
admin.site.register(Hold, HoldAdmin)
admin.site.register(LibraryBranch, LibraryBranchAdmin)
admin.site.register(LibraryCard, LibraryCardAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Status)
