from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Taggable, ArticlesTags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            print(form.cleaned_data.get('is_main'))
            if form.cleaned_data.get('is_main'):
                count += 1
        if count == 0:
            raise ValidationError('Выберите один основной тэг')
        if count > 1:
            raise ValidationError('Основной тэг должен быть один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = ArticlesTags
    formset = RelationshipInlineFormset


@admin.register(Taggable)
class TaggableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]