from django.forms import ModelForm
from polls.models import Report
from polls.models import Folder
from django.db import models
from django import forms


class ReportForm(ModelForm):
    kw = forms.CharField(required=False)
    class Meta:
        model = Report
        fields = ['subject', 'long_text', 'short_text', 'file','file2', 'private', 'datetime','location', 'kw']


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']