from offset.models import Transaction
from offset.models import Mortgage
import math
import datetime

class MortgageCalculator:
  """ mortgage account class. monthly repayment formula:
  capital * monthly rate * (1+r)^n / ( (1+r)^n-1) """
  def __init__(self, balance, rate, term, d0):
    self.c = 100.0*float(balance) # c = 170000
    self.r = float(rate) # 3.49
    self.t = term # 240
    self.s = 0.0
    self.pot_interest_accrued = 0.0
    self.m = 0.0
    self.d0 = d0
    self.today = d0
    self.to_savings = 0 # how much in one transaction goes to savings
    self.to_capital = 0 # to capital
    self.interest_paid = 0 # paid as interest
    self.interest_saved = 0 # received as offset interest
  def truncate_cent(self,amt):
    return round(amt*100,0)/100.0
  def monthly_rate(self):
    return self.r/1200.0;
  def daily_rate_approx(self,n_days=1):
    return float(n_days)*(self.r/100.0)*(1.0/360.0)
  def daily_rate(self,n_days=1):
    exponent = 1.0/360.0
    r_daily = math.pow(1.0+self.r/100.0,exponent)-1.0
    return float(n_days)*r_daily
  def monthly_repayment(self):
    if (self.m==0):
      m = self.monthly_rate()
      p = (1.0+m)**self.t
      repayment = 1.0/float(m) - 1.0/( p * m)
      repayment = float(self.c) / repayment
      self.m = math.floor(repayment) # round down to penny
      print "minimum payment: "+str(self.m/100.0)
    return self.m
  def monthly_interest(self):
    i = self.c * self.monthly_rate()
    return round(i)
  def add_daily_interest_pot(self,day):
    if (self.today > day):
      print "transaction on "+str(day)+" cannot happen before "+str(self.today)
      return
    n_days = (day-self.today).days
    interest_pot = round(self.s*self.daily_rate(n_days))
    print str(n_days)+" days interest to "+str(self.s)+" savings pot is "+str(interest_pot)
    self.pot_interest_accrued += interest_pot
    self.today = day

  def pay_lump_sum(self,amt,day):
    self.add_daily_interest_pot(day)
    print str(day)+": paid lump sum "+str(amt)
    self.s += amt
    self.to_savings = round(amt)/100.0
    self.to_capital = 0
    self.interest_paid = 0
    self.interest_saved = 0

  def pay_sum(self,amt,day):
    self.add_daily_interest_pot(day)
    self.interest_saved = self.pot_interest_accrued/100.0
    self.s = round(self.s+self.pot_interest_accrued,2)
    self.pot_interest_accrued=0
    paid = round(amt,2)
    capital_repaid = round(self.monthly_repayment() - self.monthly_interest())
    self.interest_paid = round(self.monthly_interest())/100.0
    amt -= self.monthly_interest() # pay interest
    amt -= capital_repaid # repay capital
    self.c -= capital_repaid
    self.to_capital = capital_repaid/100.0 # pennies
    self.to_savings = amt/100.0
    print "Adding "+str(round(amt,2))+" to savings pot from your "+str(paid)+" payment"
    self.s = round(self.s+amt,2) # any remaining into savings pot

  def transfer_savings(self,amt_in_pennies,date):
    """ move money from savings pot to mortgage balance"""
    # start date plus term (self.t) months
    passed_months = (date - self.d0).days / 30
    self.t = (self.t - passed_months)+1 # new term
    self.m = 0 # recompute monthly repayment
    self.add_daily_interest_pot(date)
    self.c -= amt_in_pennies # reduce capital
    self.s = self.s-amt_in_pennies # reduce po
    self.to_capital = amt_in_pennies/100
    self.to_savings = amt_in_pennies/100
    self.interest_paid = 0
    self.interest_saved = self.pot_interest_accrued/100.0
    
  def print_balances(self):
    output = "Mortgage balance: "+str(round(self.c)/100.0)
    output += "<br>"+"Savings pot: "+str(round(self.s)/100.0)
    return output

  def do_transaction(self,t):
    amt_in_pennies = 100.0*float(t.amount)
    if t.type=="SAVINGS_POT":      
        self.pay_lump_sum(amt_in_pennies,t.date)
    elif t.type == "MONTHLY":
        # pay interest and repayment, put the rest into savings pot
        self.pay_sum(amt_in_pennies,t.date)    
    elif t.type == "INTEREST":
        # a change in the interest rate
        self.add_daily_interest_pot(t.date)
        self.r = float(t.amount)
    elif t.type == "BALANCE":
        # move money from savings pot to mtg balance
        if self.s < amt_in_pennies:
	  print "error, cannot transfer "+str(amt_in_pennies)+" from a pot of "+self.s
	  return
	self.transfer_savings(amt_in_pennies,t.date)
    else:
        print "error, "+t.type+" invalid transaction type"
