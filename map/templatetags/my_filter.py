from django import template

register = template.Library()


@register.filter
def instance_str(value):
    return isinstance(value, str)
