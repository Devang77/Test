from django.contrib import admin
from .models import Member,Transaction,Book
# Register your models here.
admin.site.register(Book)
admin.site.register(Transaction)
admin.site.register(Member)
