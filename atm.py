class atm(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo

    def balanceInquiry(self):
        print("Your balance is 10000")

    def cashWithdrawal(self,amount):
        newAmount=10000-amount
        print("your balance is ", newAmount)

def main():
    cardNo=input("Enter your card number -> ")
    pinNo=input("Enter your pin number -> ")

    user1=atm(cardNo,pinNo)
    print("choose your activity")
    print("1 balance inquiry")
    print("2 cash withdrawl")

    activity=int(input("enter the activity number -> "))
    if(activity==1):
        user1.balanceInquiry()
    elif(activity==2):
        amount=int(input("Enter the amount you want to withdraw ->"))
        user1.cashWithdrawal(amount)
    else:
        print("enter a valid number")

        
main()