from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from blogs.forms import ArticleForm
from blogs.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView, LoginRequiredMixin):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blogs:article_list")

    def form_valid(self, form):
        article = form.save()
        user = self.request.user
        article.owner = user
        article.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("blogs:article_list")

    def get_success_url(self):
        return reverse("blogs:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blogs:article_list")
