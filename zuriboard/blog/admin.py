from django.contrib import admin
from .models import post

class postDB(admin.ModelAdmin):
    list_display: [
        "Title", "Text", "Author", "Created_date", "Published_date"
    ]


admin.site.register(post, postDB)