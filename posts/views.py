from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from accounts.models import UserProfile
from posts.models import Post
from comments.models import Comment
from.forms import PostForm


class PostList(ListView):
    queryset=Post.objects.all().order_by('-created_on')
    template_name='blogpage2.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        context['user_context'] = self.request.user
        return context


class PostDetail(DetailView):
    model=Post
    template_name='postpage2.html'

    
    
class PostListbyAuthor(ListView):
    model=Post
    template_name='postsbyauthor2.html'
    

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(User, pk = id)
        return Post.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['author_context'] = get_object_or_404(User, pk = self.kwargs['pk'])
        return context





def newpost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid:
            p=form.save(commit=False)
            p.author=request.user
            form.save()
            return redirect('postsbyauthor',request.user.id)

    else:
        form=PostForm()
    return render(request,'createpost.html',{'form':form})

"""def postlike(request):
    if request.method=='POST':
        post=get_object_or_404(Post,id=)"""