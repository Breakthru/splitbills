#!/usr/bin/python
# -*- coding: utf-8 -*-

# Create your views here.
from offset.models import Transaction
from offset.models import Mortgage
from django.shortcuts import render_to_response
from datetime import date
from utils import MortgageCalculator
import locale
locale.setlocale(locale.LC_ALL, '')

def calculate():
    output = ""
    display = """<table border="1">
    <tr><td>Date</td><td>Type</td><td>Amount</td>
    <td>Balance</td><td>Pot</td><td>Interest paid</td>
    <td>Interest to pot</td><td>Paid capital</td><td>Paid pot</td></tr>
    """
    transactions_list = Transaction.objects.all().order_by('date')
    mtg = Mortgage.objects.all()[0]
    mtgcalc = MortgageCalculator(balance=mtg.initial_balance, rate=mtg.initial_rate, term=mtg.term, d0=mtg.start_date)
    for t in transactions_list:
        mtgcalc.do_transaction(t)
        display += "<tr><td>"+str(t.date)+"</td><td>"+t.type+"</td>"
        display += "<td>"+str(t.amount)+"</td>"
        display += "<td>"+locale.currency(round(mtgcalc.c)/100.0,grouping=True)[1:]+"</td>"
        display += "<td>"+locale.currency(round(mtgcalc.s)/100.0,grouping=True)[1:]+"</td>"
        display += "<td>"+str(mtgcalc.interest_paid)+"</td>"
        display += "<td>"+str(mtgcalc.interest_saved)+"</td>"
        display += "<td>"+str(mtgcalc.to_capital)+"</td>"
        display += "<td>"+str(mtgcalc.to_savings)+"</td>"
        display += "</tr>"
    display += "</table>"
    output = mtgcalc.print_balances()+"<hr/>"+display

    return output

def home(request):
    mtg_list = Mortgage.objects.all()
    return render_to_response('offset/index.html', {'mtg_list': mtg_list})


def mtg(request, id):
    transactions_list = Transaction.objects.filter(mtg_id=id).order_by('-date')
    output = "<h1>Marco's mortgage calculator program</h1><hr>\n"
    output += calculate()
    context = {}
    context['calculator'] = output
    output = ""
    output += '<h2>Transactions list</h2><br><ul>'
    for t in transactions_list:
        output += '<li>'+str(t.date)+' , '+str(t.type)+' , &pound;'+str(t.amount)+'</li>'
    output += '</ul>'
    context['transactions'] = output
    return render_to_response('offset/mortgage.html', context)
