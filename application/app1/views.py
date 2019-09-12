from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PersonneForm


from .models import Personne


def list(request):
	personnes_list = Personne.objects.all()
	return render(request,'app1/pages/list.html', {'personnes_list':personnes_list})

def create(request):
	form = PersonneForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('app1:list')

	return render(request, 'app1/pages/createupdate.html', {'form':form})

def update(request, id):
	personne = Personne.objects.get(id=id)
	form = PersonneForm(request.POST or None, instance=personne)

	if form.is_valid():
		form.save()
		return redirect('app1:list') 
	return render(request, 'app1/pages/createupdate.html', {'form':form, 'personne':personne})

def delete(request, id):
	personne = Personne.objects.get(id=id)

	if request.method == 'POST':
		personne.delete()
		return redirect('app1:list')

	return render(request, 'app1/pages/delete-confirm.html', {'personne' : personne})
