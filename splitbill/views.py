from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UploadFileForm
from models import Transaction, Tag, Account, RawTransaction, Statement
from ccparser import ccparser
from datetime import date, datetime
from simple_tag import SimpleTag
import pytz
import json

def add_transactions(f, account):
    p = ccparser()
    statement = Statement()
    statement.account = account
    statement.date_added = datetime.now(pytz.utc).date()
    statement.save()
    date_from = None
    date_to = None
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
        raw.statement = statement
        raw.save()

        tr = Transaction()
        tr.raw = raw
        tr.statement = statement
        tr.date = datetime.strptime(t[fields["date"]], "%d/%m/%Y").date()
        tr.description = " ".join([t[d] for d in fields["description"]])
        tr.amount = int(100*float(t[fields["amount"]]))
        tr.account = account
        tr.save()
        # check smallest and largest date
        if not date_from:
            date_from = tr.date
        if not date_to:
            date_to = tr.date
        if date_from > tr.date:
            date_from = tr.date
        if date_to < tr.date:
            date_to = tr.date

    statement.date_from = date_from
    statement.date_to = date_to
    statement.save()

    return transactions


def test(request):
    return render(request, 'splitbill/jquery-ui.html', {})


def home(request):
    accounts = Account.objects.all()
    return render(request, 'splitbill/accounts.html', context = {'accounts': accounts})


def account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    statements = Statement.objects.filter(account_id=account_id).order_by('-date_to')
    return render(request, 'splitbill/statements.html', context = {'account': account, 'statements': statements})


def statement(request, statement):
    t_list = Transaction.objects.filter(statement_id=statement).order_by('-date')
    context = { 'transactions': t_list }
    return render(request, 'splitbill/transactions.html', context)


def autotag(request, statement):
    rule_tags = SimpleTag()
    transactions = Transaction.objects.filter(statement_id=statement)
    for tr in transactions:
        rule_tags.tag(tr)
    return HttpResponseRedirect(reverse("splitbill.statement", kwargs={'statement': statement}))

def upload(request, account):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            t = add_transactions(request.FILES['file'], get_object_or_404(Account, pk=account))
            return HttpResponseRedirect(reverse("splitbill.account", kwargs={'account_id': account}))
    else:
        form = UploadFileForm()
        context = {'form':form, 'account':get_object_or_404(Account, pk=account)}
        return render(request, 'splitbill/upload.html', context)
