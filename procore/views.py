from django.contrib.auth.models import User
from django.db import models
from procore.models import Post
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import RedirectView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comments, Like
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

class PostVoteToggle(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Post, pk=self.kwargs['pk'])
        url_ =obj.get_absolute_url()
        User = self.request.user
        if User.is_authenticated():
            if User in obj.votes_total.all():
                obj.votes_total.remove(User)
            else:
                obj.votes_total.add(User)

        return url_

class PostListView(ListView):
    model = [Post]
    template_name = ''

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'content','image']