#PROPERTY PURCAHSED- $133,000

#INCOME 
#Rental Income - $1,500 
#TMI - $1,500/monthly 

#EXPENSES 
#Property Tax: $1,440/YEARLY - $120/MONTHLY
#HOA: $407/MONTHLY
#INSURANCE: $250/YEARLY - $20.83/MONTHLY
#UTILITIES: $0
#VACANCY/REPAIRS: $100/MONTHLY
#MORTGAGE: $505/MONTHLY
#TME - $1,152.83

#CASH FLOW
#$1,500 - $1,152.83 = $347.17
#TMCF: $347.17

#CASH ON CASH- ROI
#Downpayment: $13,000
#Closing Costs: $3,300
#Rehab: $10,000
#TOTAL INVESTMENT - $26,300
#ANNUAL CASH FLOW - $4,166.04

#ROI = $4,166.04 / $26,300 = 15.84%

#DEFINE THE CLASS 
#NameofClass 
class Investment: 
    def __init__(self, rental_income=0, other_income=0, taxes=0, renovations=0, mortgage=0, repairs=0, vacancy=0, insurance=0, hoa=0, 
                 other_expenses=0, downpayment=0, closing_costs=0, other_purchase_costs=0, utility=0):
        self.rental_income = rental_income + other_income
        self.expenses = taxes + renovations + mortgage + repairs + vacancy + insurance + hoa + other_expenses 
        self.cashoncash = downpayment + closing_costs + other_purchase_costs

    #define Total Monthly Income 
        def TotalMonthlyIncome(self):
            while True:
                rental_income = float(input("Enter the annual rental income."))
                if rental_income > 0:
                    break
                else: 
                    print("Please enter a valid number or 0.")
                
            while True:
                other_income = float(input("Enter any other income, if applicable:"))
                if other_income >= 0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            TMI = rental_income + other_income
            return TMI
    
    #define Total Monthly Expenses
        def TotalMonthlyExpense(self):
            while True:
                renovations = float(input("Enter total cost of renovations."))
                if renovations >= 0:
                    break
                else:
                    print("Please enter a valid number or 0.")
            
            while True: 
                repairs = float(input("Enter total cost of repairs."))
                if repairs >= 0: 
                   break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                taxes = float(input("Enter yearly property taxes."))
                if taxes >= 0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                mortgage = float(input("Enter yearly cost of mortgage."))
                if mortgage >= 0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True: 
                vacancy = float(input("Enter yearly reserve costs for vacancy."))
                if vacancy >=0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                insurance = float(input("Enter yearly cost of home insurance."))
                if insurance >0: 
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                hoa = float(input("Enter the yearly cost of HOA."))
                if hoa >0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                utility = float(input("Enter the yearly utilties expense, if applicable."))
                if utility >0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True: 
                other_expenses = float(input("Enter total cost of other expenses, if applicable."))
                if other_expenses >0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            TME = taxes + renovations + mortgage + repairs + vacancy + insurance + hoa + other_expenses + gas_electric_water
            return TME
        
        #define the Cash on Cash Flow 
        def CashonCashFlow(self): 
            while True: 
                downpayment = float(input("Enter total cost of redownpayment."))
                if downpayment >0:
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:        
                closing_costs = float(input("Enter total cost of closing costs."))
                if closing_costs >0: 
                    break
                else:
                    print("Please enter a valid number or 0.")

            while True:
                other_purchase_costs = float(input("Enter total cost of other purchase costs."))
                if other_purchase_costs >0: 
                    break
                else:
                    print("Please enter a valid number or 0.")

            COC = downpayment + closing_costs + other_purchase_costs
            return COC

        #define the ROI
        def ROIcalculations(self): 
            TMI = self.rental_income
            TME = self.expenses
            COC = self.cashoncash

            Annual_Profits = TMI - TME
            EROI = (Annual_Profits / COC)
            PROI = EROI * 100
            return EROI

        def runner(self):
            while True:
                introquestion = input("Thank you for choosing Alicia ROI Calculater today! Let's go ahead and click begin, please enter all data with a valid number.")
                if (introquestion == "begin"):
                    tmi = self.TotalMonthlyIncome()
                    tme = self.TotalMonthlyExpense()
                    coc = self.CashonCashFlow()
                    roi = self.ROIcalculations()

                    print(f'Total Monthly Income: {tmi}')
                    print(f'Total Monthly Expense: {tme}')
                    print(f'Total Monthly Cash on Cash Flow: {coc}')
                    print(f'Your ROI Calculation: {roi}')
                
                else:
                    print("Invalid, please click BEGIN or END to proceed.")

projectinvestment = Investment()


