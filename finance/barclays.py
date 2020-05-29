#!/usr/bin/env python3

import sys
import re


def barclays_convert(fp):
    """Number,Date,Account,Amount,Subcategory,Memo"""
    fp.readline() # read header line
    transactions = []
    while True:
        line = fp.readline()
        if not line:
            break
        d = line.strip().split(',')
        date = d[1]
        amount = d[3]
        description = d[4]+" "+d[5]
        transactions.append("%s,%s,%s" % (date, description, amount))
    return transactions


def main():
    with open(sys.argv[1],'r', encoding='latin_1') as fp:
        transactions = barclays_convert(fp)

    # print transactions in reverse order
    for i in range(len(transactions)-1,-1,-1):
        print(transactions[i])

if __name__ == "__main__":
    main()

