balance = 320000
annualInterestRate = 0.2
MonthlyInterestRate = annualInterestRate / 12.0
MonthlyPayment_low = balance / 12
MonthlyPayment_high = (balance * (1 + MonthlyInterestRate)**12) / 12.0
Payment = (MonthlyPayment_low + MonthlyPayment_high) / 2

def PaymentCalc(Amount, Balance, rate_monthly, pay_low, pay_high):

    '''Takes in a value for Balance and starting value for a monthly Payment,
       for the highest and lowest monthly payments.
       Returns Balance, the sum of starting balance and Interrest,
       with a given monthly payment.'''

    for i in range(12):
        UnpaidBalance = Balance - Amount
        Balance = UnpaidBalance + rate_monthly*UnpaidBalance

    '''Checks, if 12 of the given monthly Payments are the smallest
       Amount to settle the account
       Returns the lowest payment.'''

    if Balance > 0.1:
        pay_low = Amount
        Amount = (pay_low + pay_high) / 2
        PaymentCalc(Amount, balance, MonthlyInterestRate, pay_low, pay_high)
    elif Balance < -0.1:
        pay_high = Amount
        Amount = (pay_low + pay_high) / 2
        PaymentCalc(Amount, balance, MonthlyInterestRate, pay_low, pay_high)
    else:
        print('Lowest payment: ', round(Amount, 2))


PaymentCalc(Payment, balance, MonthlyInterestRate, MonthlyPayment_low, MonthlyPayment_high)
