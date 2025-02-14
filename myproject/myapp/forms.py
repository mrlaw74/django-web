from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=Task.PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Task
        fields = ['title', 'completed', 'due_date', 'priority']

    # Ensure priority has a default value
    def clean_priority(self):
        priority = self.cleaned_data.get('priority', 'Medium')  # Default to 'Medium'
        if not priority:
            return 'Medium'
        return priority