from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Candidate, CandidateAwards


class CandidateInline(admin.TabularInline):
    model = Candidate
    fk_name = 'awards'
    extra = 1
    fields = ('name', 'photo',  "description",'number_of_votes')
    readonly_fields = ('number_of_votes',)

@admin.register(CandidateAwards)
class CandidateAwardsAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'image', 'get_candidates')
    search_fields = ('translations__name', 'slug')
    inlines = [CandidateInline]
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'description', 'image'),
        }),
        ('Дополнительно', {
            'fields': ('slug',),
        }),
    )

    def get_candidates(self, obj):
        return ", ".join(c.name for c in obj.candidates.all())
    get_candidates.short_description = 'Кандидаты'

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'awards', "description", 'number_of_votes')
    search_fields = ('name',)
    list_filter = ('awards',)
