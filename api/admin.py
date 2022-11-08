from django.contrib import admin

from api.models import Author, Book, Payment, User

# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Payment)
