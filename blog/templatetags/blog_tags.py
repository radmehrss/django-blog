from django import template
from blog.models import POST,Comment
from blog.models import category
from taggit.models import Tag

register = template.Library()

@register.inclusion_tag('blog/latest_post.html')
def latestposts():
    posts = POST.objects.filter(status=1).order_by('-published_date')
    return {'posts':posts}

@register.inclusion_tag('blog/post-category.html')
def postcategory():
    posts = POST.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'cat_dict':cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/blog-tags.html')
def posttags():
    tags = Tag.objects.all()
    return {'tags': tags}