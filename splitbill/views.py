from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from models import Transaction, Tag

def home(request):
    t_list = Transaction.objects.all()
    context = {'name': 'world', 'msg': 'file not valid','transactions': t_list}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            context['msg'] = 'valid'
            for line in request.FILES['file']:
                print line
        return HttpResponseRedirect('/splitbill')
    else:
        form = UploadFileForm()
        context['form'] = form

    return render(request, 'splitbill/index.html', context)
