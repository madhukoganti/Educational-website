from django import forms
from app1.models import Student,Contact



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'     


