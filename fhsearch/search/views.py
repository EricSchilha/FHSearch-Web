from django.shortcuts import render
from django.http import HttpResponse
from .models import Stats

# Create your views here.
def index(request):
    query_results = Stats.objects.all()
    fields = Stats._meta.get_fields()
    context = {'query_results': query_results, 'fields': fields}
    return render(request, 'list.html', context)
