from django.contrib import admin

from .models import Language, Tag, Snippet

admin.site.register((Language, Tag, Snippet))
