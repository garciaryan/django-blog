from django.contrib import admin
from .models import Post
from .fields import UserSelectWidget
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        widgets = {
            'author': UserSelectWidget,
        }

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostAdmin)
