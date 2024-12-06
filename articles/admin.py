from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag_list = []
        for form in self.forms:
            flag_list.append(form.cleaned_data['is_main'])
        for _ in flag_list:
            if True not in flag_list:
                raise ValidationError('Укажите основной раздел')
            elif flag_list.count(True) > 1:
                raise ValidationError('Уже есть основной раздел')
            else:
                continue
        return super().clean()

class ScopesInline(admin.TabularInline):
    model = Scopes
    extra = 0
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopesInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
