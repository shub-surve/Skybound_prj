from django import template

register = template.Library()

@register.filter
def multiply_by_100(value):
    try:
        return int(value) * 100
    except (ValueError, TypeError):
        return value  # return the value as is if there's an error
