from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.db.models import Q
from .models import post
from .forms import PostForm

# Create your views here.

def post_list(request):
    query = post.objects.all().order_by('-publish')
    q = request.GET.get('q')
    if q:
        query = query.filter(
            Q(title__icontains=q)|
            Q(user__username__icontains=q))
    paginator = Paginator(query, 5)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    #select * from post
    # user = request.user
    # if request.user.is_authenticated:
    #     context = {
    #     'user':user
    #     }
    # else:
    #     context = {
    #         'user':user
    #     }
    context  = {
        'views_title':'list',
        'query' : queryset
    }
    return render(request, "list.html", context)

def post_detail(request, id):
    # instance = post.objects.get(id=index)
    instance = get_object_or_404(post, id=id)
    context ={
        'views_title':'detail',
        'dato' : instance
    }
    return render(request,"detail.html", context)
#crear una njueva publicacion
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Exitosamente creado')
    context = {
        'views_title':'create',
        'btn':'Crear',
        'form':form
    }
    return render(request,"form.html", context)

#actualizar publicacion
def post_update(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    instance = get_object_or_404(post, id=id)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Item salvado')
        return HttpResponseRedirect(instance.get_url())
    context = {
        'views_title':'update',
        'instance' : instance,
        'btn':'Editar',
        'form':form
    }
    return render(request,"form.html", context)
#eliminar publicacion
def post_delete(request, id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    instance = get_object_or_404(post, id=id)
    instance.delete()
    messages.success(request, 'Eliminado exitosamente')
    return redirect('index')