from django.contrib import admin

from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 2

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]

admin.site.register(Category)