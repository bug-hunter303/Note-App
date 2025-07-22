from django import forms
from Note_app.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color: #1e1e1e; color: white;',
                }),
            
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'style': 'background-color: #1e1e1e; color: white;',
            }),
        }