from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'legal_expert']  # Assuming 'legal_expert' is the optional field
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4}),
            'legal_expert': forms.Select(attrs={'class': 'form-control'}),  # Add styling if needed
        }
        labels = {
            'question_text': 'Your Question',
            'legal_expert': 'Ask a Specific Expert (Optional)',
        }