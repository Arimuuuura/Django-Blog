from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin # ログインが必須になる

class IndexView(View): # ホーム画面
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html', {
            'post_data': post_data
        })

class PostDetailView(View): # 投稿詳細画面
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data': post_data
        })

class CreatePostView(LoginRequiredMixin, View): # 新規投稿画面
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        # 新規投稿ボタンを押したときにフォーム画面へリダイレクト
        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs): # 投稿ボタンを押したときにコールされる
        form = PostForm(request.POST or None)

        if form.is_valid(): # post formの内容をチェック
            post_data = Post() # postの内容を代入
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save() # DBに保存
            return redirect('post_detail', post_data.id) # 詳細画面にリダイレクト

        return render(request, 'app/post_form.html', {
            'form': form
        })