from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post' :post,
#     })
    
post_detail = DetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")