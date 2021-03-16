class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber 
        self.pinNumber  = pinNumber 

    def CashWithdrawl(self, amountofMoney):
        self.amountofMoney = amountofMoney
       
    def BalanceEnquiry(self, moneyLeft):
        self.moneyLeft = moneyLeft
        

Aadit = Atm("Aadit", 230, 123456, (amountofMoney(2000)), (moneyLeft(15000)) )
Aditi = Atm("Aditi", 231, 654321, (amountofMoney(3000)), (moneyLeft(15000)) )

print(Aadit(13000))
print(Aditi(12000))
