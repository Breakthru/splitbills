#!/usr/bin/env python3

import sys
import re


def tesco_convert(fp):
    """Date			Card no.			Description				Money in	Money out"""
    transactions = []
    while True:
        line = fp.readline().rstrip('\r\n')
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
        transactions.append("%s;%s;%s;%s" % (date, cardno, description, amount))
    return transactions


def main():
    with open(sys.argv[1],'r', encoding='latin_1') as fp:
        transactions = tesco_convert(fp)

    # print transactions in reverse order
    for i in range(len(transactions)-1,-1,-1):
        print(transactions[i])

if __name__ == "__main__":
    main()

