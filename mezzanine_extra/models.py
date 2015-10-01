#encoding: utf-8
from django.db import models
from mezzanine.core.models import Orderable, RichText
from mezzanine.pages.models import Page, RichTextPage
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.utils.models import upload_to


class PageImage(Orderable):
    """
    An image for a richtext page.
    """
    page = models.ForeignKey(RichTextPage, verbose_name="Page", null=True, blank=True, related_name="images")
    file = FileField("Fichier", max_length=200, format="Image",
                     upload_to=upload_to("PageImage.file", "pages"))
    description = models.CharField("Description", blank=True, max_length=200)

    class Meta:
        verbose_name = "Image"


class PageBlock(Orderable, RichText):
    """
    A block for a richtext page.
    """
    page = models.ForeignKey(RichTextPage, verbose_name="Page", null=True, blank=True, related_name="blocks")
    title = models.CharField("Titre", max_length=200, default="")
    image = FileField("Image", upload_to="staticblocks", format="Image", max_length=255, null=True, blank=True)
    short_content = RichTextField(u"Description courte", blank=True)
    css_class = models.CharField(max_length=200, default="", blank=True)

    class Meta:
        verbose_name = "Bloc statique"
        verbose_name_plural = "Blocs statiques"

    def __unicode__(self):
        return self.title


class Person(Orderable):
    first_name = models.CharField("First name", max_length=100)
    last_name = models.CharField("Last name", max_length=100)
    updated = models.DateTimeField("Updated at", auto_now=True)