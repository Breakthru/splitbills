from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UploadFileForm
from models import Transaction, Tag, Account
from ccparser import ccparser
from datetime import date, datetime

def add_transactions(f, account):
    p = ccparser()
    if (account.type == "TESCO"):
        p.parseTescoBank(f)
    else:
        raise Exception("Account %s bad type %s" % (account.name, account.type))
    for line in p.transactions:
        fields = line.split(';')
        tr = Transaction()
        tr.date = datetime.strptime(fields[0],'%Y-%m-%d').date()
        tr.description = fields[2]
        tr.amount = int(100.0*float(fields[3]))
        tr.account = account
        tr.save()


def test(request):
    return render(request, 'splitbill/jquery-ui.html', {})


def home(request):
    t_list = Transaction.objects.all().order_by('-date')
    context = { 'transactions': t_list }
    return render(request, 'splitbill/index.html', context)
    

def upload(request, account):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            add_transactions(request.FILES['file'], get_object_or_404(Account, pk=account))
            return HttpResponseRedirect(reverse('splitbill.home'))
    else:
        form = UploadFileForm()
        context = {'form':form, 'account':get_object_or_404(Account, pk=account)}
        return render(request, 'splitbill/upload.html', context)
