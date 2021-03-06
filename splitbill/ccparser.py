#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re
import logging
import csv

def remove_non_ascii(s):
  return ''.join([i for i in s if ord(i) < 128])

class ccparser:
  """parser for santander and tesco credit card report files"""

  def parseTescoBank(self, fileToParse):
    """ transaction list will be in self.transactions """
    json_out = []
    reader = csv.reader(fileToParse)
    header = None
    for row in reader:
        if not header:
            header = [s.strip() for s in row]
        else:
            transaction = {}
            for i in range(len(header)):
                transaction[header[i]] = remove_non_ascii(row[i])
            json_out.append(transaction)
    return json_out


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
    transactions = p.parseTescoBank(fp)
  # print transactions in reverse order
  for t in transactions:
    print t
