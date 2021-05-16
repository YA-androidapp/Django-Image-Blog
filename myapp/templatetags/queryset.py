from django import template


register = template.Library()

@register.filter(name='get_list_from_queryset')
def get_list_from_queryset(queryset, key):
    return queryset.values(key, flat=True)


@register.filter(name='count_queryset_id')
def count_queryset_id(queryset, id):
    if queryset:
        if queryset.count() > 0:
            return queryset.filter(id=id).count()
    return None