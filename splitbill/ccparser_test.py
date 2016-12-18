# -*- coding: UTF-8 -*-
import unittest
from StringIO import StringIO
from ccparser import ccparser

# Create your tests here.
class CCParserTest(unittest.TestCase):
    def test_example_report(self):
        f = StringIO("""
Transaction Date, Posting Date, Billing Amount, Merchant, Merchant City , Merchant State , Merchant Zip , Reference Number , Debit/Credit Flag , SICMCC Code
19/09/2016,20/09/2016,£10.55,"MERCHANT A","Example PC",,PC0 5EA,1234567890,D,1234
19/09/2016,20/09/2016,£5.69,"MERCHANT PLC SACA","Example",GBR,PC 8NB,123456789,D,1234
""")
        p = ccparser()
        p.parseTescoBank(f)
        self.assertEqual(len(p.transactions), 2)
    	self.assertTrue( "10.55" in p.transactions[0])


if __name__=="__main__":
    unittest.main()
