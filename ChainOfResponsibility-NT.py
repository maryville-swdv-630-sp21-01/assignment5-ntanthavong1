class Paycheck():

    def __init__(self, EBIT, taxExempt, stateTaxRate, federalTaxRate, socialSecurityTaxRate, medicareTaxRate):
        self.EBIT = EBIT # Earning Before Interest and Taxes
        self.taxExempt = taxExempt
        self.stateTaxRate = stateTaxRate
        self.federalTaxRate = federalTaxRate
        self.socialSecurityTaxRate = socialSecurityTaxRate
        self.medicareTaxRate = medicareTaxRate
        self.netPayment = EBIT

    def taxPaycheck(self):
        if self.taxExempt == True:
            return self.EBIT
        else:
            self.applyStateTax()

    def applyStateTax(self):
        deduction = self.EBIT * self.stateTaxRate
        self.netPayment = self.netPayment - deduction
        self.applyFederalTax()

    def applyFederalTax(self):
        deduction = self.EBIT * self.federalTaxRate
        self.netPayment = self.netPayment - deduction
        self.applySocialSecurityTax()

    def applySocialSecurityTax(self):
        deduction = self.EBIT * self.socialSecurityTaxRate
        self.netPayment = self.netPayment - deduction
        self.applyMedicareTax()

    def applyMedicareTax(self):
        deduction = self.EBIT * self.medicareTaxRate
        self.netPayment = self.netPayment - deduction
        return self.netPayment

# Tax Exempt
paycheck = Paycheck(5000, True, .1, .08, .062, .0145)
paycheck.taxPaycheck()
print(paycheck.netPayment)

# Not Tax Exempt
paycheck = Paycheck(5000, False, .1, .08, .062, .0145)
paycheck.taxPaycheck()
print(paycheck.netPayment)