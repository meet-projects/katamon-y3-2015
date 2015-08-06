from django import template
import datetime

register = template.Library()


@register.filter
def html_classes(event):
    return " ".join(event.getHtmlClasses())


@register.filter
def get_range(value):
    """
      Filter - returns a list containing range made from given value
      Usage (in template):

      <ul>{% for i in 3|get_range %}
        <li>{{ i }}. Do something</li>
      {% endfor %}</ul>

      Results with the HTML:
      <ul>
        <li>0. Do something</li>
        <li>1. Do something</li>
        <li>2. Do something</li>
      </ul>

      Instead of 3 one may use the variable set in the views
    """
    return range(1, value + 1)


@register.filter
def get_event_times(event):
    endDate = datetime.datetime(event.date.year, event.date.month,
                                event.date.day, event.date.hour + event.duration, event.date.minute)

    return event.date.strftime("%H:%M") + " ~ " + endDate.strftime("%H:%M")


@register.filter
def category_html_class(category):
    return category.getCategoryClassName()
