from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from blog.models import POST,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse

def blog_view(request,author_username=None,**kwargs):
    published_posts = POST.objects.filter( published_date__lt = timezone.now())
    unpublished_posts = POST.objects.filter( published_date__gt = timezone.now())
    if author_username:
        published_posts = published_posts.filter(author__username=author_username)
    if kwargs.get('tag_name')!=None:
        published_posts = published_posts.filter(tags__name__in=[kwargs['tag_name']])
    published_posts = Paginator(published_posts,2)
    try:
        page_number = request.GET.get('page')
        published_posts = published_posts.get_page(page_number)
    except PageNotAnInteger:
        published_posts = published_posts.get_page(1)
    except EmptyPage:
        published_posts = published_posts.get_page(1)
    context = {'published_posts':published_posts,'unpublished_posts':unpublished_posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited')
        else:
            messages.add_message(request,messages.ERROR,"your comment didn't submited")
    posts = POST.objects.filter( published_date__lt = timezone.now())
    post = get_object_or_404(posts,pk=pid)
    next_post = POST.objects.filter(published_date__gt = post.published_date).order_by('published_date').first()
    previous_post = POST.objects.filter(published_date__lt = post.published_date).order_by('-published_date').first()
    if not post.login_require or request.user.is_authenticated:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        context = {'post':post,'next_post':next_post,'previous_post':previous_post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(f"{reverse('accounts:login')}?next={request.path}")
def test(request):
    post = POST.objects.filter(status=1)
    context = {"post":post}
    return render(request,'test.html',context)

def blog_cat(request,cat_name):
    posts = POST.objects.filter(status=1)
    published_posts = posts.filter(category__name=cat_name)
    context = {'published_posts':published_posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    published_posts = POST.objects.filter(status=1)
    if request.method == 'GET':
        published_posts = published_posts.filter(content__contains=request.GET.get('s'))
    context = {"published_posts":published_posts}
    return render(request,'blog/blog-home.html',context)