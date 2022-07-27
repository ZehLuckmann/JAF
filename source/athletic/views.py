from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AthleticForm
from .models import Athletic

from django.contrib.auth import get_user_model
User = get_user_model()

def athletic_index(request):
    athletic = Athletic.objects.all()
    context = {'athletic': athletic}
    return render(request, 'athletic/index.html', context)


def athletic_add(request):  
    if request.method == "POST":  
        form = AthleticForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/athletic')  
            except:  
                pass  
    else:  
        form = AthleticForm() 

    return render(request,'athletic/add.html',{'form':form}) 

def athletic_edit(request, athletic_id):
    athletic = Athletic.objects.get(id=athletic_id)
    form = AthleticForm(initial={'initials': athletic.initials, 'name': athletic.name, 'logo': athletic.logo})
    print(athletic.logo)
    if request.method == "POST":  
        form = AthleticForm(request.POST, request.FILES , instance=athletic)  
        print(form.instance.logo)
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/athletic')  
            except Exception as e: 
                pass    
    return render(request,'athletic/edit.html',{'form':form}) 
    
def athletic_delete(request, athletic_id):
    athletic = get_object_or_404(Athletic, pk=athletic_id)
    athletic.delete()
    return HttpResponseRedirect('/athletic')

def athletic_users(request, athletic_id):
    athletic = get_object_or_404(Athletic, pk=athletic_id)
    users = User.objects.filter(athletic=athletic_id).all()
    context = {'users': users, 'athletic' : athletic}
    return render(request, 'athletic/users.html', context)

def athletic_disapprove(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_member = False
    user.save()
    return HttpResponseRedirect(f'/athletic/users/{user.athletic.id}')

def athletic_approve(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_member = True
    user.save()
    return HttpResponseRedirect(f'/athletic/users/{user.athletic.id}')

def athletic_promove(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_board = True
    user.save()
    return HttpResponseRedirect(f'/athletic/users/{user.athletic.id}')