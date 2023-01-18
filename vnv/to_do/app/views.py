from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .models import Task
from .forms import AddTaskForm,UpdateForm
from django.contrib import messages


def index(request):
   
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Adding..')
            return HttpResponseRedirect('/')
    else:
        form = AddTaskForm()   
    data = Task.objects.all()
    return render(request,'index.html',{"data":data,"form":form})


def delete(request,id):
	task = Task.objects.get(id=id)
	task.delete()
	return HttpResponseRedirect('/')




def update_view(request,id):
    template = "update_view.html"
    context = {}
        
    obj = get_object_or_404(Task, id=id)
    form = UpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
        
    context["form"] = form
    
    return render(request, template, context)
    
    
    
    
# def create_view(request):
#     template = "create_view.html"
#     context = {}

#     form = MyModelForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()

#             return HttpResponseRedirect('/thanks/')

#     context["form"] = form
#     return TemplateResponse(request, template, context)