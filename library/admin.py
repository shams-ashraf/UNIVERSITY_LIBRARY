from django.contrib import admin # type: ignore
from .models import Book, borrowedb, userProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'author', 'published_year', 'publisher', 'quantity', 'category')

@admin.register(borrowedb)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('borrower_name', 'telephone', 'national_id', 'isbn', 'start_date', 'due_date', 'email', 'remaining_days')

@admin.register(userProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin')

