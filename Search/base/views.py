from django.shortcuts import render, redirect
import json
from .forms import searchform
from .models import client
# Create your views here.

def search(request):
    form = searchform()
    names = client.objects.values_list('firstname', flat=True)
    names = list(names)
    names = json.dumps(names)

    if request.method == 'POST':
        form = searchform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect('result', name)
    context = {
        'form': form,
        'name': names
    }
    return render(request, 'Search.html', context)

def result(request, name):
    item = client.objects.filter(firstname=name)
    context = {
        'result': item
    }
    return render(request, 'Result.html', context)