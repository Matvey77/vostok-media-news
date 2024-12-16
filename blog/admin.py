from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'author', 'views', 'category', 'slug', 'created_at', 'render_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id', 'author')
    list_filter = ('category', 'tags', 'author')
    readonly_fields = ('id', 'views', 'created_at', 'render_photo')
    fields = (
        'id', 'title', 'slug', 'views',
        'category', 'tags', 'author', 'content', 'created_at', 'photo', 'render_photo'
    )
    save_on_top = True

    def render_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="200">')
        return '-'

    render_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
