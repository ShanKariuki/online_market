from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category' , 0)
    categories=Category.objects.all()
    items=Item.objects.filter(is_sold=False)
    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request, 'store/items.html',{'items':items
                                               ,
                                               'query':query,
                                               'categories':categories,
                                               'category_id':int(category_id)})





def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    context={'items':items,
             'categories':categories}
    return render(request,'store/index.html', context)

def about(request):
    context={}
    return render(request,'store/about.html', context)

def detail(request,id):
    item=get_object_or_404(Item,pk=id)
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(id=id)[0:3]
    context={'item':item,
             'related_items':related_items}
    return render(request,'store/detail.html', context)
@login_required
def newitem(request):
    if request.method =="POST":
        form=NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('store:detail',id=item.id)
    else:
        form=NewItemForm()
    return render(request,'store/item.html', {
        'form':form,
        'title':'New Item',
    })
@login_required
def edititem(request,id):
    item=get_object_or_404(Item,id=id,created_by=request.user)
    if request.method =="POST":
        form=EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('store:detail',id=item.id)
    else:
        form=EditItemForm(instance=item)
    return render(request,'store/item.html', {
        'form':form,
        'title':'Edit  Item',
    })
@login_required
def delete(request,id):
    item=get_object_or_404(Item,id=id,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')