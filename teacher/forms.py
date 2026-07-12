from django import forms
from . models import Teacher

class Teacher_Form(forms.ModelForm):
   class Meta:
         model=Teacher
         fields="__all__"

   def cleanedsub(self):
       subject=self.cleaned_data.get("subject")

       if len(subject)<3:
              raise forms.ValidationError("invalid input")

       return subject
 