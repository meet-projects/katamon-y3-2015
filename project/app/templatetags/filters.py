from django import template

register = template.Library()


@register.filter
def html_classes(event):
    return " ".join(event.getHtmlClasses())
