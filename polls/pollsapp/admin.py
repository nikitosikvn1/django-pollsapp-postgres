from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question_id", "choice", "votes")


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)