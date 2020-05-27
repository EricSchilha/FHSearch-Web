from django.shortcuts import render
from django.http import HttpResponse

from .models import Stats
from .filters import StatsFilter

# Create your views here.
def index(request):
    query_results = Stats.objects.all()
    fields = Stats._meta.get_fields()

    filter = StatsFilter(request.GET, queryset=query_results) # Send data to filter
    query_results = filter.qs # Set results to filtered data

    context = {'query_results': query_results, 'fields': fields, 'filter': filter}

    return render(request, 'results.html', context)
