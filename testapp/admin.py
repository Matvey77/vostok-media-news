from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Rubric, Article


class RubricAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Rubric, RubricAdmin)
admin.site.register(Article)
