from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.inclusion_tag('tags/liked_status.html', takes_context=True)
def liked_status(context, obj):
    user = context['user']
    is_liked = False
    url = reverse('toggle_like', args=(obj.id,))
    if user.is_authenticated:
        is_liked = obj.likes.filter(id=user.id).exists()
        #TODO check if liked
        #HINT blog.likes.filter(id=user.id).exists()

        return {
            'user': user,
            'is_liked': is_liked,
            'url': url,
            'obj': obj,
        }
