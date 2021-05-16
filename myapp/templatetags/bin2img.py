from django import template
import base64


register = template.Library()

@register.filter(name='bin2img')
def bin2img(binary):
    return base64.b64encode(binary).decode('utf-8')
