from django.views.generic import ListView
from articles.models import Article


class ArticlesList(ListView):
    template_name = 'articles/news.html'
    queryset = Article.objects.all()
    # ordering = '-published_at'
    context_object_name = 'object_list'
