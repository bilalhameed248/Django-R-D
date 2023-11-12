from django.shortcuts import render, redirect
from .forms import Personal_Info_Form
from .forms import PI_Edit_Form
from .models import personal_info
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def insert_data(request):
    if request.method=="POST":
        form= Personal_Info_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list/')
    else:
        form= Personal_Info_Form()
    return render(request, "crud/insert_form.html", {'form':form})

def list_data(request):
    context= {'list_data' : personal_info.objects.all()}
    return render(request, "crud/list_record.html", context)

def update_data(request, id):
    if request.method=="GET":
        personal_data=personal_info.objects.get(pk=id)
        form= PI_Edit_Form(instance=personal_data)
        return render(request, "crud/edit_form.html", {'form':form})
    elif request.method=="POST":
        personal_data=personal_info.objects.get(pk=id)
        form= PI_Edit_Form(request.POST, request.FILES, instance=personal_data)
        if form.is_valid():
            form.save()
        return redirect('/crud/list')

def delete_data(request, id):
    data=personal_info.objects.get(pk=id)
    data.delete()
    return redirect('/crud/list')
