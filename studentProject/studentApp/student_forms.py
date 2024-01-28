from django import forms
class STUDENTS(forms.Form):
    Reg_no=forms.CharField()
    Name=forms.CharField()
    Email_id=forms.CharField()
    Department=forms.CharField()
    Semester=forms.CharField()
    Attendance=forms.CharField()
    Cgpa=forms.CharField()
class srch(forms.Form):
    Name=forms.CharField()
    Department=forms.CharField()
class delet(forms.Form):
    Name=forms.CharField()
    Department=forms.CharField()
class updat(forms.Form):
    Reg_no=forms.CharField()
    Semester=forms.CharField()
    Cgpa=forms.CharField()