from django import forms

class NumberForm(forms.Form):
    numbers = forms.CharField(label='Enter numbers (comma-separated)', widget=forms.TextInput(attrs={'class': 'form-control'}))
