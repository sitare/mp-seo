
import seo.translation

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from seo.models import PageMeta


class PageMetaAdmin(TranslationAdmin):
    list_display = ('url', 'title', 'robots', )
    list_editable = ('robots', )


admin.site.register(PageMeta, PageMetaAdmin)
