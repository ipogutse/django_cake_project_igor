from django.shortcuts import render, redirect
from .models import Studentdata, Coursedata
from django.db.models import Q

# Create your views here.

def qset(request):
    # data1 = Studentdata.objects.all().values()
    data1 = Studentdata.objects.all().values('sid')
    data2 = Studentdata.objects.filter(sid='S001', course_id='C001').values()
    data3 = Studentdata.objects.filter(Q(sid='S001') | Q(course_id='C001')).values()
    data4 = Studentdata.objects.filter(sid='S001').values()|Studentdata.objects.filter(course_id='C001').values()
    data5 = Studentdata.objects.filter(Q(name='john') | Q(name='rose')).values()
    data6 = Studentdata.objects.filter(name__startswith='j').values()
    context = {'d1': data1, 'd2': data2, 'd3': data3, 'd4': data4, 'd5': data5, 'd6': data6}
    return render(request, 'studentinfo.html', context=context)
    
def studentinfo(request):
    course1 = Coursedata(course_id='C001', course_name='python', duration='30')
    course1.save()

    course2 = Coursedata(course_id='C002', course_name='java', duration='30')
    course2.save()
    
    course = Coursedata.objects.get(course_id='C001')
    student1 = Studentdata(sid='S001', name='john', course=course)
    student1.save()
    
    student2 = Studentdata(sid='S002', name='rose', course=course)
    student2.save()

    course2 = Coursedata.objects.get(course_id='C002')
    student3 = Studentdata(sid='S003', name='rose1', course=course2)
    student3.save()

    print('data added successfully....................')

    # Studentdata.objects.filter(name='rose').delete()
    Coursedata.objects.filter(course_name='java').delete()
    
    fetch1 = Studentdata.objects.get(sid='S001')
    student_name = fetch1.name
    course_name = fetch1.course.course_name
    print ('Student name: ', student_name, 'course: ', course_name)
    return render(request, 'studentinfo.html', {'course_name': course.course_name})
    # return redirect('/')


# from django.shortcuts import render
# from .models import Studentdata,Coursedata
# # Create your views here.
# def studentinfo(request):
#     course1= Coursedata(course_id='C001',course_name='python',duration='30')
#     course1.save()

#     student1=Studentdata(sid='S001',name='john',course=course1.course_id)
#     student1.save()
#     print("data added successfully.................")
#     return render(request,"helllooooo we are working on moedels")
    