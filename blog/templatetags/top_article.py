from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/top_article_tpl.html')
def get_top_article(category=None):
    if category:
        top_article = Post.objects.filter(category=category).order_by('-views').first()
    else:
        top_article = Post.objects.order_by('-views').first()
    return {'post': top_article}