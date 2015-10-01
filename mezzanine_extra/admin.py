#encoding: utf-8
from copy import deepcopy
from mezzanine_advanced_admin.admin import SortableInline, CollapsibleInline, SortableAdmin
from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, register
from mezzanine.pages.models import RichTextPage
from mezzanine.pages.admin import PageAdmin as MezzaninePageAdmin
from .models import PageImage, PageBlock, Person


class PageImageAdmin(SortableInline, TabularInline):
    model = PageImage
    extra = 0


class PageBlockAdmin(SortableInline, CollapsibleInline, StackedInline):
    model = PageBlock
    extra = 0
    exclude = ("content", "short_content")


inlines = deepcopy(MezzaninePageAdmin.inlines)
inlines.extend([PageImageAdmin, PageBlockAdmin])
class PageAdmin(MezzaninePageAdmin):
    inlines = inlines


admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, PageAdmin)


class PersonAdmin(SortableAdmin, admin.ModelAdmin):
    list_display = ("last_name", "first_name",)
    list_editable = ("first_name",)
    date_hierarchy = "updated"


admin.site.register(Person, PersonAdmin)
