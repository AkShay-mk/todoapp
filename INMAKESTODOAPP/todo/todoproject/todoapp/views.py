from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib import messages
from django.http import HttpResponse

class tasklistview(ListView):
    model=Task
    template_name='add.html'
    context_object_name='task1'
    
class taskdetailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task2'
    
class taskupdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task3'
    fields=('task','priority','date')
    def get_success_url(self) -> str:
        return reverse_lazy('taskdetailview',kwargs={'pk':self.object.id})
    
class taskdeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    context_object_name='task3'
    success_url=reverse_lazy('tasklistview')

def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        tas=Task(task=name,priority=priority,date=date)
        tas.save()
    
        
    return render(request,'add.html',{'task1':task1})

def delete(request,tas_id):
    task1=Task.objects.get(id=tas_id)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')
    
def edit(request,ta_id):
    task1=Task.objects.get(id=ta_id)
    fo=todoform(request.POST or None,instance=task1)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':fo,'task1':task1})
    
    