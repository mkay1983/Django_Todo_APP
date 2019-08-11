from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder':'Get Milk, Do laundry,..',
                            'aria-label':'Text input with dropdown button'
    }))
