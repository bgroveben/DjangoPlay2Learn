import random
import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def repeat(value, times=2):
    return value * times

@register.filter
def clean(value):
    cusses = ['stupid', 'stinky', 'darn', 'shucks', 'crud', 'dirt']
    for cuss in cusses:
        cuss_re = re.compile(re.escape(cuss), re.IGNORECASE)
        chars = ''.join([random.choice('!@#$%^&*') for letter in cuss])
        value = cuss_re.sub(chars, value)
    return value
from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter(name='mention', is_safe=True)
@stringfilter
def mention(value):
    my_list = value.split()
    for i in my_list:
        if i[0] == '@':
            try:
                stng = i[1:]
                user = User.objects.get(username=stng)
                if user:
                    profile_link = user.userprofile.get_absolute_url()
                    i = f"<a href='{profile_link}'>{i}</a>"
                    res = res + i + ' '
                    return mark_safe(res)
            except User.DoesNotExist:
                return value
        else:
            return value
