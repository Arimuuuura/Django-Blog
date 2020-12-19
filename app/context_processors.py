from .models import Category

# 全てのカテゴリデータをどのテンプレートでも取得できるようにする
def common(request):
    category_data = Category.objects.all()
    context = {
        'category_data': category_data
    }
    return context