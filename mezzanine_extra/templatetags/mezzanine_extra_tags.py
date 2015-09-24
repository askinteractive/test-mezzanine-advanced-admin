try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict
from django.db import models
from django.template.context import RequestContext
from mezzanine import template
from mezzanine.conf import settings
from mezzanine.forms.forms import FormForForm
from mezzanine.forms.models import Form


register = template.Library()


@register.filter
def class_name(value):
    """
    Get model verbose name.
    """
    if(isinstance(value, models.Model)):
        return value._meta.verbose_name
    return type(value)


@register.as_tag
def get_menus_for_page(page):
    menus = []
    for menu in settings.PAGE_MENU_TEMPLATES:
        if str(menu[0]) in page.in_menus:
            menus.append(menu[1])
    return menus

@register.as_tag
def get_content_model_for_page(page):
    content_models = {
        'link': u"Lien",
        'form': u"Formulaire",
        'richtextpage': u"Page",
        'gallery': u"Galerie"
    }
    return content_models[page.content_model]


@register.as_tag
def get_contact_form(request):
    """
    Retrieve a form by its slug.
    :param slug:
    :return:
    """
    page_form = Form.objects.filter(slug='contact').first()
    if page_form:
        form = FormForForm(page_form, context=RequestContext(request))
        new_fields = OrderedDict()
        for name, field in form.fields.iteritems():
            if field.required:
                new_fields[name] = field
            elif field.help_text == "event":
                field.choices[0] = ('', field.label)
                new_fields[name] = field
        form.fields = new_fields
        return {'page': page_form, 'form': form}
    return