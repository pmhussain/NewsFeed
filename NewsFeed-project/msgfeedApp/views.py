from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url='login')
def Feedpage(request):
    form = MessageForm()
    if request.method == 'POST':
        #user = User.objects.get(username=request.user)
        user = request.user.username
        message = request.POST.get('message')
        image = request.FILES.get('image')

        new_post = Message.objects.create(person=user, message=message, image=image)
        print(new_post)
        new_post.save()

        # form = MessageForm(request.POST,request.FILES)
        # print(form.is_valid())
        # if form.is_valid():
        #     form.save()

    messages = Message.objects.all().order_by('-created_date')
    context = {
    'messages':messages,
    'form':form
    }
    return render(request, 'msgfeedApp/msgfeed.html',context)

@login_required(login_url='login')
def likepost(request,message_id):
    user = request.user.username
    #message_id = request.GET.get('message_id')
    message_obj = Message.objects.get(id=message_id)
    #print("message",message)
    like_filter = Like.objects.filter(Like_id=message_id, username=user).first()
    if like_filter == None:
        new_like = Like.objects.create(Like_id=message_id, username=user)
        new_like.save()
        message_obj.no_of_likes = message_obj.no_of_likes + 1
        message_obj.save()
    else:
        like_filter.delete()
        message_obj.no_of_likes = message_obj.no_of_likes - 1
        message_obj.save()

    return redirect('feed')

@login_required(login_url='login')
def commentpost(request,message_id):
    form = MessageForm()
    #print(form)
    user = request.user.username
    #message_id = request.GET.get('message_id')
    message_obj = Message.objects.get(id=message_id)
    if request.method == 'POST':
        #user = User.objects.get(username=request.user)
        user = request.user.username
        print(user)
        comment = request.POST.get('message')
        print(comment)
        new_comment= Comment.objects.create(comment_id=message_id, username=user, comment=comment)
        new_comment.save()
        #image = request.FILES.get('image')
        # comment_filter = Comment.objects.filter(comment_id=message_id, username=user).first()
        #
        # if comment_filter == None:
        #     new_comment= Comment.objects.create(comment_id=message_id, username=user, comment=comment)
        #     print(new_comment)

        from django.http import HttpResponseRedirect
        path = request.path_info
        return HttpResponseRedirect(path)

    comments = Comment.objects.all()
    #messages = Message.objects.get()
    print('message_obj$$$',message_obj.person, message_obj.id,message_id)
    context = {
    'comments':comments,
    'form':form,
    'message_id':message_id,
    'user': user
    }
    return render(request, 'msgfeedApp/comments.html', context)

@login_required(login_url='login')
def editcomment(request,pk):
    comment = Comment.objects.get(id=pk)
    form = MessageForm()
    context ={ 'comment' : comment, 'form':form,}
    if request.method=='POST':
        #print(request.POST.get('message'))
        #print(comment.comment)
        comment.comment=request.POST.get('message')
        comment.save()
        #print(comment.comment)
        return redirect('commentpost', comment.comment_id)
    return render (request, 'msgfeedApp/edit.html', context)

@login_required(login_url='login')
def deletecomment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = MessageForm()
    context ={ 'comment' : comment, 'form':form,}
    if request.method=='POST':
        comment.delete()
        return redirect('commentpost', comment.comment_id)
    return render (request, 'msgfeedApp/delete.html', context)
