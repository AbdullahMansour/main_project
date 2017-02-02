from django.contrib import admin

from .models import Question
from .models import Choice, Question
from django.contrib import admin
# Register your models here.



admin.site.register(Choice)

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuiestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic', {'fields' :['question_text']}),
        ('Data Information', {'fields' : ['pub_date']}),
    ]

    inlines = [ChoiceInLine]

admin.site.register(Question, QuiestionAdmin)