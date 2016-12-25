from django.test import TestCase
from django.test import Client
from splitbill.views import add_transactions
from splitbill.models import Account
from StringIO import StringIO

# Create your tests here.
class TestAddTransactions(TestCase):
    def test_add_transactions(self):
        f = StringIO("""
Transaction Date, Posting Date, Billing Amount, Merchant, Merchant City , Merchant State , Merchant Zip , Reference Number , Debit/Credit Flag , SICMCC Code
19/09/2016,20/09/2016,10.55,"MERCHANT A","Example PC",,PC0 5EA,1234567890,D,1234
19/09/2016,20/09/2016,5.69,"MERCHANT PLC SACA","Example",GBR,PC 8NB,123456789,D,1234
""")
        account = Account()
        account.type = "TESCO"
        account.save()
        transactions = add_transactions(f, account)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["Billing Amount"], "10.55")


class TestUpload(TestCase):
    def test_csv(self):
        c = Client()
        response = c.post('/upload')
        self.assertEqual(response.status_code, 404)
