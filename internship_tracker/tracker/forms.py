from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        # fields = ['student_name', 'department', 'company', 'start_date', 'end_date', 'role']
        fields='__all__'
