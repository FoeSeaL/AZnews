from newspaper.models import Category,Post,Tag

def nav(request):
    categories=Category.objects.all()[:3]
    tags =Tag.objects.all()[:12]
    recent_posts=Post.objects.filter(
            published_at__isnull=False, status="active"
            
    ).order_by("-published_at")
    side_categories = Category.objects.all()[:6]
    return {
        "categories":categories,
        "tags":tags,
        "recent_posts":recent_posts,
        "side_categories":side_categories
    }