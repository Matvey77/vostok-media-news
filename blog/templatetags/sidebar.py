from django import template
from django.db.models import Count
from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_post(count=3):
    posts = Post.objects.order_by('-views')[:count]
    return {"posts": posts}

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags(count=5):
    tags = Tag.objects.annotate(posts_count=Count('posts'))
    tags = tags.order_by('-posts_count')[:count]
    return {"tags": tags}
