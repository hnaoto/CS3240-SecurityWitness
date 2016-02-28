from django.contrib import admin
from polls.models import Question
from polls.models import Report
from polls.models import Folder


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,               {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date']}),
                 ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Report)
admin.site.register(Folder)