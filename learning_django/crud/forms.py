from django import forms
from .models import personal_info

class Personal_Info_Form(forms.ModelForm):
    class Meta:
        model=personal_info
        fields='__all__'
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'upload':'Upload CV'
        }

class PI_Edit_Form(forms.ModelForm):
    class Meta:
        model=personal_info
        fields=('first_name', 'last_name', 'upload')
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'upload':'Upload CV'
        }