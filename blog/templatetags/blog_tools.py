@register.inclusion_tag('tags/liked_status.html', takes_context=True)
def liked_status(context, obj):
    user = context['user']
    is_liked = False
    url = reverse('toggle_like')
    if user.is_authenticated:
        #TODO check if liked
        #HINT blog.likes.filter(id=user.id).exists()

    return {
        'user': user,
        'is_liked': is_liked,
        'url': url,
        'obj': obj,
    }
