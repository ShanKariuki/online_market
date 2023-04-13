from django.shortcuts import render,redirect,get_object_or_404
from store.models import Item
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request, item_pk):
    item=get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    
    conversations=Comm.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations:
        return redirect('comm:detail', pk=conversations.first().id)

    if request.method =='POST':
        form=CommMessageForm(request.POST)

        if form.is_valid():
            conversation=Comm.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()


            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()


            return redirect( 'store:detail', pk=item_pk)
        
    else:
        form=CommMessageForm()

    return render(request, 'comm/new.html',{'form':form})    

@login_required
def inbox(request):
    conversations=Comm.objects.filter(members__in=[request.user.id])

    return render(request,'comm/inbox.html',{
        'conversations':conversations
    })


@login_required
def detail(request, pk):
    conversation=Comm.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == "POST":
        form=CommMessageForm(request.POST)
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            conversation.save()

            return redirect('comm:detail', pk=pk)
    else:
        form=CommMessageForm()


    return render(request, 'comm/detail.html',{'conversation':conversation,
                                               'form':form
                                               })



                