from django.shortcuts import render
from django.shortcuts import redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    data = Blog.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'blog/index.html', params)

def create(request):
    params = {
        'form': BlogForm(),
    }
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog(title=title, content=content)
        blog.save()
        return redirect(to='/blog')
    return render(request, 'blog/create.html', params)


def detail(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	params = {
            'id': blog_id,
        	'obj': blog,
        }
	return render(request, 'blog/detail.html', params)


def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect(to='/blog')
    else:
        form = BlogForm(initial={
            'title': blog.title,
            'content': blog.content,
        })
        params = {
            'id': blog_id,
            'form': form,
        }
        return render(request, 'blog/edit.html', params)

def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.delete()
        return redirect(to='/blog')
    else:
        params = {
            'id': blog_id,
            'obj': blog,
        }
        return render(request, 'blog/delete.html', params)
