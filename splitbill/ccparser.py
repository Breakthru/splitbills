#!/usr/bin/python

import sys
import re
import logging

class ccparser:
  """parser for santander credit card report file"""
  def __init__(self):
    self.transactions=[]

  def parseTescoBank(self, fileToParse):
    """ transaction list will be in self.transactions """
    for line in fileToParse:
      fields = line.split('\t')
      if len(fields)!=9:
          continue
      for i in range(9):
          print "[%s]: %s" % (i, fields[i])
      date = fields[0].strip()
      cardno = fields[2].strip()
      description = fields[4].strip()
      try:
          money_in = float(fields[7])
      except ValueError:
          money_in = 0

      try:
          money_out = float(fields[8])
      except ValueError:
          money_out = 0

      amount = money_out - money_in
      self.transactions.append("%s;%s;%s;%s" % (date, cardno, description, amount))


  def parseSantander(self, f):
    """ f is the file object to parse """
    while True:
    # Date			Card no.			Description				Money in	Money out
        line = f.readline().rstrip('\r\n')
        if not line:
            break
        d=line.split('\t')
        idx=len(d)-1
        amount=0
        try:
            if d[idx]:
                amount=float(d[idx])
            else:
                # if last element is null, next is money-in
                while not d[idx]:
                  idx=idx-1
                amount=-float(d[idx])
        except Exception as e:
            continue
        # next non-empty is description
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        description=d[idx]
        # next non-empty is card number
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        cardno=d[idx]
        # next non-empty is date
        idx=idx-1
        while not d[idx]:
            idx=idx-1
        date=d[idx]
        # sometimes there's no card number
        if idx<0:
            date=cardno
            cardno=''
        self.transactions.append("%s;%s;%s;%s" % (date, cardno, description, amount))


if __name__=='__main__':
  p = ccparser()
  with open(sys.argv[1],'r') as fp:
    p.parseTescoBank(fp)
  # print transactions in reverse order
  for t in p.transactions:
    print t
