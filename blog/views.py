from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'


class BlogDetailView(DetailView): 
    model = Post
    template_name = "post_detail.html"
    
class BlogCreateView(LoginRequiredMixin, CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body"]  # Removed 'author' - will be set automatically
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super().form_valid(form)


    
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields =  ['title','body']

class BlogDeleteView(LoginRequiredMixin, DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")