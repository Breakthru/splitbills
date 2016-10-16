#!/usr/bin/python
# -*- coding: utf-8 -*-

# Create your views here.
from offset.models import Order
from offset.models import Transaction
from offset.models import Mortgage
from django.shortcuts import render
from datetime import date, timedelta
from dateutil import relativedelta
from utils import MortgageCalculator
import locale
locale.setlocale(locale.LC_ALL, '')


def build_transaction_list(mortgage):
    transactions = []    
    order_list_r = Order.objects.all().order_by('-date')    
    # bank orders are until the mortgage term, or until the next order
    end_date = mortgage.start_date + relativedelta.relativedelta(months=mortgage.term)
    for o in order_list_r:
        period = []
        if o.type=="MONTHLY":
            delta = relativedelta.relativedelta(end_date, o.date)
            months = delta.years*12 + delta.months
            for m in range(months):
                t = Transaction()
                t.date = o.date + relativedelta.relativedelta(months=m)
                t.type = "MONTHLY"
                t.amount = o.amount
                t.mtg = mortgage
                period.append(t)
        end_date = o.date
        period.reverse()
        transactions += period
    
    transactions.reverse()
    return transactions

def calculate():
    output = ""
    display = """<table border="1">
    <tr><td>Date</td><td>Type</td><td>Amount</td>
    <td>Balance</td><td>Pot</td><td>Interest paid</td>
    <td>Interest to pot</td><td>Paid capital</td><td>Paid pot</td></tr>
    """    
    mtg = Mortgage.objects.all()[0]
    transactions_list = build_transaction_list(mtg) #Transaction.objects.all().order_by('date')
    mtgcalc = MortgageCalculator(balance=mtg.initial_balance, rate=mtg.initial_rate, term=mtg.term, d0=mtg.start_date)
    for t in transactions_list:
        mtgcalc.do_transaction(t)
        display += "<tr><td>"+str(t.date)+"</td><td>"+t.type+"</td>"
        display += "<td>"+str(t.amount)+"</td>"
        display += "<td>"+str(round(mtgcalc.c)/100.0)+"</td>"
        display += "<td>"+str(round(mtgcalc.s)/100.0)+"</td>"
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
    return render(request, 'offset/index.html', context={'mtg_list': mtg_list})


def mtg(request, id):
    transactions_list = Transaction.objects.filter(mtg_id=id).order_by('-date')
    output = calculate()    
    # output = ""
    # output += '<h2>Transactions list</h2><br><ul>'
    # for t in transactions_list:
    #     output += '<li>'+str(t.date)+' , '+str(t.type)+' , &pound;'+str(t.amount)+'</li>'
    # output += '</ul>'
    # context['transactions'] = output    
    return render(request, 'offset/mortgage.html', {'table': output})
