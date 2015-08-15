from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from models import Transaction, Tag
from santander.ccreport import ccparser
from datetime import date, datetime

def add_transactions(f):
    p = ccparser()
    p.parse(f)
    for line in p.transactions:
        fields = line.split(';')
        tr = Transaction()
        tr.date = datetime.strptime(fields[0],'%Y-%m-%d').date()
        tr.description = fields[2]
        tr.amount = int(100.0*float(fields[3]))
        tr.save()


def home(request):
    t_list = Transaction.objects.all()
    context = {'name': 'world', 'msg': 'file not valid','transactions': t_list}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            context['msg'] = 'valid'
            add_transactions(request.FILES['file'])
    else:
        form = UploadFileForm()
        context['form'] = form

    return render(request, 'splitbill/index.html', context)
