from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Category
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
            category = form.cleaned_data['category'] # formから入力されれたカテゴリの取得
            category_data = Category.objects.get(name=category) # Category model から取得したカテゴリでフィルターをかけてデータを取得
            post_data.category = category_data #カテゴリデータをポストデータに登録
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save() # DBに保存
            return redirect('post_detail', post_data.id) # 詳細画面にリダイレクト

        return render(request, 'app/post_form.html', {
            'form': form
        })

class PostEditView(LoginRequiredMixin, View): #投稿の編集
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = { #form の初期データに出力される
                'title': post_data.title,
                'category': post_data.category,
                'content': post_data.content,
                'image': post_data.image,
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs): #編集画面から投稿した時の処理
        form = PostForm(request.POST or None)

        if form.is_valid(): # post formの内容をチェック
            post_data = Post.objects.get(id=self.kwargs['pk']) # postの内容を代入
            post_data.title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            category_data = Category.objects.get(name=category)
            post_data.category = category_data
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.save() # DBに保存
            return redirect('post_detail', self.kwargs['pk']) # DBのデータを書き換える

        return render(request, 'app/post_form.html', {
            'form': form
        })

class PostDeleteView(LoginRequiredMixin, View): #投稿の削除
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs): #削除するボタンを押したら index にリダイレクト
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_data = Category.objects.get(name=self.kwargs['category']) #URL からカテゴリー名そ取得してカテゴリモデルでフィルタをかけてデータを取得
        post_data = Post.objects.order_by('-id').filter(category=category_data)
        return render(request, 'app/index.html', {
            'post_data': post_data
        })