from .models import Category, Tag


def category_tag_cloud(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return {
        'category_cloud': categories,
        'tag_cloud': tags
    }
