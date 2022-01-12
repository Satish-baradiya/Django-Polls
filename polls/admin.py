from django.contrib import admin
from .models import Question,  Choice

# Register your models here.
class Choiceline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information',{'fields' : ['pub_date']}),
    ]
    inlines = [Choiceline]

admin.site.register(Question,QuestionAdmin)

