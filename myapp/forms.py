from django import forms
from .models import MyModel
from django.forms.widgets import DateInput


class DateInput(forms.DateInput):
    input_type = 'date'


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        #fields = ["STUDENT_NO", "STUDENT_NAME", "STUDENT_DOB", "STUDENT_DOJ"]
        #labels = {"STUDENT_NO":"STUDENT_NO", "STUDENT_NAME":"STUDENT_NAME", "STUDENT_DOB":"STUDENT_DOB", "STUDENT_DOJ":"STUDENT_DOJ" }
        widgets = {
            'STUDENT_DOB': DateInput(),
            'STUDENT_DOJ': DateInput()
        }