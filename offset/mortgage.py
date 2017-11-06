class Mortgage:
    def __init__(self, b, r, t):
        self.balance = b
        self.rate = r
        # term in months
        self.term = t
    def repayment(self):
        # monthly rate
        m = self.rate / 1200.0
        p = (1.0+m)**self.term
        return m*self.balance*p / (p-1.0)
    def step(self):
        interest = self.balance*self.rate/1200.0
        tot = self.repayment()
        cap = tot - interest
        print("repaid %s goes %s in interest and %s in capital" % (tot, interest, cap))
        self.balance -= cap
        self.term -= 1
