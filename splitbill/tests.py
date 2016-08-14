from django.test import TestCase
from StringIO import StringIO
from ccparser import ccparser

# Create your tests here.
class CCParserTest(TestCase):
    def test_example_report(self):
        f = StringIO("""2003-09-012003-11-015423
        Date			Card no.			Description				Money in	Money out
        -------------------------------------------------------------------------------------------------------------------------------
        2003-09-05		** 5423		PURCHASE - DOMESTIC            LONDON                                 				8.48
        2003-09-05		** 5423		PURCHASE - DOMESTIC            LONDON                                 				11.10
""")
        p = ccparser()
        p.parseTescoBank(f)
        self.assertEqual(len(p.transactions), 2)
