from django import template

register = template.Library()
@register.filter(name = 'cut')
def cut(value,arg):
    """
        This replaces the arg with whatever 
    """
    return value.replace(arg, '')

#register.filter('cut', cut) used decorator above