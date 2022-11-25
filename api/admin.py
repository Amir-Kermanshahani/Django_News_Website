from django.contrib import admin
from api.models import Category, Post , Contact

#Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('title','author', 'created_at', 'released', 'featured')
    list_filter = ('released', 'featured')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ['name', 'subject', 'email']

admin.site.register(Contact, ContactAdmin)