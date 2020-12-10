from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # ホーム画面にアクセスがあったときに index.html に飛ぶ
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]