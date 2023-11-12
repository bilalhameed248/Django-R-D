from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student
from .models import Section
from .forms import Student_Info_Form
from .forms import Section_Form
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def student_list(request):
	form= Student_Info_Form()
	context= {'student_list' : Student.objects.all(), 'section_list' : Section.objects.all(),'form':form}
	return render(request, "student_register/student_list.html",context)

def insert_student(request):
	if request.method=="POST":
		student_id = request.POST.get('student_id')
		fullname = request.POST.get('fullname')
		roll_no = request.POST.get('roll_no')
		mobile = request.POST.get('mobile')
		section_id = request.POST.get('section_id')
		if student_id is not None:
			Student.objects.filter(pk=student_id).update(fullname=fullname,roll_no=roll_no,mobile=mobile,section_id=section_id)
			return redirect('/students')
		elif student_id is None:
			form = Student_Info_Form(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/students')
			else:
				return HttpResponse("Invalid Form")
	else:
		return redirect('/students')

def edit_student(request):
	if is_ajax(request=request):
		edit_id = request.POST.get('id')
		student = Student.objects.get(id=edit_id)
		# serialize in new participant object in json
		ser_instance = serializers.serialize('json', [ student, ])
		# send to client side.
		return JsonResponse({"instance": ser_instance}, status=200)
	else:
		return redirect('/students')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def delete_student(request, id):
	student=Student.objects.get(pk=id)
	student.delete()
	return redirect('/students')
	
def insert_section(request):
	if request.method=="POST":
		form = Section_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/students')
		else:
			return HttpResponse("Invalid Form")
	else:
		return redirect('/students')