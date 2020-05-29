#!/usr/bin/env python3
import os
from santander import santander_convert

def test_conversion():
    with open("test.txt", "w") as fp:
        fp.write("""From: 01/01/2019 to 02/02/2020

     Account: XXXX XXXX XXXX 4419

    Date: 02/01/2020
    Description: test description test description
    Amount: -100.00
    Balance: 200.00

    Date: 01/01/2020
    Description: test description test description
    Amount: -100.00
    Balance: 100.00
                                                        """)

    with open("test.txt",'r') as fp:
        transactions = convert(fp)

    # print transactions in reverse order
    for i in range(len(transactions)-1,-1,-1):
        print(transactions[i])

    os.remove("test.txt")

if __name__=="__main__":
    test_conversion()
