from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from blogs.models import Article


class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter +=1
        self.object.save()
        return self.object

class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "preview", "is_published")
    success_url = reverse_lazy('blogs:article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "preview", "is_published")
    success_url = reverse_lazy('blogs:article_list')

    def get_success_url(self):
        return reverse('blogs:article_detail', args=[self.kwargs.get('pk')])

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blogs:article_list')
