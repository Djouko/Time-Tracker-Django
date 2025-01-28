from django import forms
from .models import TimeLog
from django.utils import timezone

class TimeLogForm(forms.ModelForm):
    class Meta:
        model = TimeLog
        fields = ['description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].initial = timezone.now()
        self.fields['end_time'].initial = timezone.now()