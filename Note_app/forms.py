from django import forms
from Note_app.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'maxlength': 10,
                'rows': 3,
                'style': 'background-color: #1e1e1e; color: white;',
            }),
        }