from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# • Use a specific QuerySet instead of retrieving all objects. Instead of defining
# a queryset attribute, you could have specified model = Post and Django
# would have built the generic *Post.objects.all()* QuerySet for you.
# • Use the context variable posts for the query results. The default variable is
# *object_list* if you don't specify any context_object_name.
# • Paginate the result, displaying three objects per page.
# • Use a custom template to render the page. If you don't set a default template,
# ListView will use blog/post_list.html.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    object_list = Post.published.all()
    # 添加分页
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # 输入的页码不是整数
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:  # 没有输入页码
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # *render* takes the request object, the template path, and the context variables to render the given template.
    # It returns an HttpResponse object with the rendered text (normally HTML code).
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    # *get_object_or_404* retrieves the object that matches the given parameters or an
    # HTTP 404 (not found) exception if no object is found.
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
