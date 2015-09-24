# encoding: utf-8
from django import forms
from django.forms.util import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from mezzanine.pages.models import Page


class PageWidget(forms.TextInput):

    def __init__(self, attrs=None, default_value=None, select_label="or choose a page"):
        self.default_value = default_value
        self.select_label = select_label
        super(PageWidget, self).__init__(attrs)

    class Media:
        js = ['admin/js/pagewidget.js']


    def get_pages(self):
        """
        Return all site pages.
        :return: Pages
        """
        return Page.objects.published().order_by('title')

    def render_pages_select(self, value=None):
        """
        Render a <select> with published pages.
        :return: string
        """
        html = '&nbsp;<span>%s</span><select class="pagewidget" id="pagewidget_%s" data-input-id="%s">%s</select>'
        options = []
        if not self.default_value is None:
            options.append('<option value="%s">%s</option>' % ('', self.default_value))
        for page in self.get_pages():
            selected = " selected" if page.get_absolute_url() == value else ""
            options.append('<option value="%s"%s>%s</option>' % (page.get_absolute_url(), selected, page.title))
        return html % (self.select_label, self.attrs['name'], self.attrs['id'], "\n".join(options))


    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        self.attrs = final_attrs
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return format_html('<input{0} /> %s' % self.render_pages_select(value), flatatt(final_attrs))