from django.shortcuts import render,get_object_or_404,redirect

from store.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)
    context={'items':items}
    return render(request, 'dashboard/index.html',context)


