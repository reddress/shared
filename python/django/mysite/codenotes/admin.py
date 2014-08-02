from django.contrib import admin
from .models import Tag, Language, Post, Sample

# Register your models here.
admin.site.register(Tag)
admin.site.register(Language)
# admin.site.register(Post)
admin.site.register(Sample)

class SampleInline(admin.StackedInline):
    model = Sample
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [SampleInline]

admin.site.register(Post, PostAdmin)
