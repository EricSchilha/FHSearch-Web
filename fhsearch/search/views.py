from django.shortcuts import render
from django.http import HttpResponse
from .models import PlayerData

# Create your views here.
def index(request):
    query_results = PlayerData.objects.all()
    context = {'query_results': query_results}
    return render(request, 'list.html', context)
