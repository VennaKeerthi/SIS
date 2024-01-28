from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from studentApp.models import STUDENTS as S
from studentApp.student_forms import STUDENTS
from studentApp.student_forms import srch,delet,updat
# Create your views here.

def home(request):
    return render(request,"home.html")

def add(request):
    ack=""
    student=STUDENTS()
    if request.method=='POST':
        student=STUDENTS(request.POST)
        if student.is_valid():
            sid=student.cleaned_data["Reg_no"]
            name=student.cleaned_data["Name"]
            email=student.cleaned_data["Email_id"]
            dep=student.cleaned_data["Department"]
            sem=student.cleaned_data["Semester"]
            att=student.cleaned_data["Attendance"]
            cgpa=student.cleaned_data["Cgpa"]
            st=S(s_reg=sid,s_name=name,s_email=email,s_department=dep,s_semester=sem,s_attendance=att,s_cgpa=cgpa)
            st.save()
            ack="Added successfully ..."
            return render(request,"ack.html",{'text':ack})
    return render(request,"insert.html",{'form1':student})

def search(request):
    f1=srch(request.POST or None)
    if f1.is_valid():
        n=f1.cleaned_data["Name"]
        d=f1.cleaned_data["Department"]
        queryset=S.objects.filter(s_name=n,s_department=d)
        if len(queryset)==0:
            return render(request,"ack.html",{'text':'Student not found ...'})
        context={
            'Title':'Searched data is found...', 
            'Queryset':queryset
        }
        return render(request,"existing.html",context)
    return render(request,"search.html",{'form2':f1})

def delete(request):
    title=""
    f2=delet(request.POST or None)
    if f2.is_valid():
        n=f2.cleaned_data["Name"]
        d=f2.cleaned_data["Department"]
        queryset=S.objects.filter(s_name=n,s_department=d)
        queryset.delete()
        title="Deleted successfully ..."
        return render(request,"ack.html",{'text':title})
    return render(request,"delete.html",{'form3':f2})

def display(request):
    queryset=S.objects.all()
    context={
        "Title":"Display all Students details",
        "Queryset":queryset
    }
    return render(request,"existing.html",context)

def update(request):
    f4=updat(request.POST or None)
    if f4.is_valid():
        i=f4.cleaned_data["Reg_no"]
        j=f4.cleaned_data["Semester"]
        m=f4.cleaned_data["Cgpa"]
        queryset=S.objects.get(s_reg=i)
        queryset.s_semester=j
        queryset.s_cgpa=m
        queryset.save()
        x=S.objects.filter(s_reg=i)
        context={
        "Title":"Updated successfully...",
        "Queryset":x
        }
        return render(request,"existing.html",context)
    return render(request,"update.html",{'form4':f4})  