from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UploadFileForm
from models import Transaction, Tag, Account, RawTransaction
from ccparser import ccparser
from datetime import date, datetime
from simple_tag import SimpleTag
import pytz
import json

def add_transactions(f, account):
    p = ccparser()
    if (account.type == "TESCO"):
        transactions = p.parseTescoBank(f)
        fields = {}
        fields["date"] = "Transaction Date"
        fields["amount"] = "Billing Amount"
        fields["description"] = ["Merchant", "Merchant City", "Merchant State", "Merchant Zip"]
    else:
        raise Exception("Account %s bad type %s" % (account.name, account.type))
    for t in transactions:
        raw = RawTransaction()
        raw.raw_data = json.dumps(t)
        raw.date_added = datetime.now(pytz.utc).date()
        raw.account = account
        raw.save()

        tr = Transaction()
        tr.raw = raw
        tr.date = datetime.strptime(t[fields["date"]], "%d/%m/%Y").date()
        tr.description = " ".join([t[d] for d in fields["description"]])
        tr.amount = int(100*float(t[fields["amount"]]))
        tr.account = account
        tr.save()

        rule_tags = SimpleTag()
        rule_tags.tag(tr)

    return transactions


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
            t = add_transactions(request.FILES['file'], get_object_or_404(Account, pk=account))
            return HttpResponseRedirect(reverse("home"))
    else:
        form = UploadFileForm()
        context = {'form':form, 'account':get_object_or_404(Account, pk=account)}
        return render(request, 'splitbill/upload.html', context)
