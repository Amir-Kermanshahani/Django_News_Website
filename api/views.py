from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Post, Category
from django.views.generic import TemplateView 
from django.views import generic
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import ContactForm






# Create your views here.



class IndexView(ListView):

    model = Post
    template_name="index.html"
    context_object_name = 'data'

    categories = Category.objects.all()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        featured_posts = Post.objects.filter(released=1, featured=1)
        latest_posts = Post.objects.filter(released=1).order_by('-created_at')
        context['categories'] = self.categories
        context['featured_posts'] = featured_posts
        context['latest_posts'] = latest_posts
    
        
        return context


class Contact(FormView):

    context_object_name = 'data'
    categories = Category.objects.all()
    form_class = ContactForm
    template_name = "contact.html"
    success_url = 'index'

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        try:
            context['message'] = self.message
        except:
            pass
        
        return context

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        message = "Your information has been saved. We'll reach you as soon as possible!"
        return render(request, 'contact.html', {'message':message})



class Single(DetailView):   

    model = Post
    template_name = "single.html"
    context_object_name = 'post'

    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(released=1).order_by('-created_at')
    categories = Category.objects.all()
    #comments = Comment.objects.filter(status=1, post = Post_id)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tags'] = self.tags
        context['latest_posts'] = self.latest_posts
        context['categories'] = self.categories

        return context



#The View to display posts related to specific category
class CategoryView(ListView):

    template_name = "category.html"
    model = Post
    context_object_name = 'data'
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest_posts = Post.objects.filter(released=1).order_by('-created_at')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, title=self.kwargs['cat'])
        category_posts = Post.objects.filter(released=1, category=category)
        context['category'] = category
        context['category_posts'] = category_posts  
        context['categories'] = self.categories
        context['tags'] = self.tags
        context['latest_posts'] = self.latest_posts
        
        return context

