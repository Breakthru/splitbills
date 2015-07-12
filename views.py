from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from models import *

# Create your views here.
def home(request):
    transactions_list=Transaction.objects.all()
    context = RequestContext(request, {'transactions_list':transactions_list})
    return render_to_response('splitbills/index.html', context)
