
from django.contrib import admin
from .models import About, Review, Coffee, Images, Post, Tag, Subscribe


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    filter_horizontal = ('tags',)
    search_fields = ('title', 'price')


admin.site.register(About)
admin.site.register(Review)
admin.site.register(Coffee)
admin.site.register(Images)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe)
admin.site.register(Tag)
