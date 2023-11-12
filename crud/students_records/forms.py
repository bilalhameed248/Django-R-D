from django import forms
from .models import Student
from .models import Section
class Student_Info_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'fullname':'Full Name',
            'roll_no':'Roll No',
            'mobile':'Mobile No',
            'section_id':'Section Id'
        }

class Section_Form(forms.ModelForm):
    class Meta:
        model=Section
        fields='__all__'
        labels={
            'section_title':'Section Title'
        }
