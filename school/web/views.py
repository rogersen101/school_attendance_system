from django.shortcuts import render, redirect
from .models import Student

def homePage(request):
    all_students = Student.objects.all()
    context = {
        "students": all_students
    }
    return render(request, 'index.html', context)


def addPage(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get("name"),
            student_id=request.POST.get("student_id"),
            is_present=request.POST.get("is_present") == "on"
        )
        return redirect('/')

    return render(request, 'add.html')


def viewPage(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'view.html', {'student': student})


def editPage(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.student_id = request.POST.get('student_id')
        student.is_present = request.POST.get('is_present') == 'on'
        student.save()
        return redirect('/')

    return render(request, 'edit.html', {'student': student})


def deletePage(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('/')

    return render(request, 'delete.html', {'student': student})