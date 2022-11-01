from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "date")
    search_fields = ['question']
    list_filter = ['date']

    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ("question_id", "choice", "votes")


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)