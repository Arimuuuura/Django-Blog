from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # ホーム画面にアクセスがあったときに index.html に飛ぶ
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'), #投稿の編集画面
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'), #投稿の削除
    path('category/<str:category>', views.CategoryView.as_view(), name='category'), #投稿の設定(str を設定することでカテゴリの名前がURLになる)
    path('search/', views.SearchView.as_view(), name='search'), #検索ページ
]