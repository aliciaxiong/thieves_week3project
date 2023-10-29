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
class Investment: 
    def __init__(self, rental_income, other_income, taxes, renovations, mortgage, repairs, vacancy, insurance, hoa, other_expenses, downpayment, closing_costs, utilities, other_purchase_costs):
        self.rental_income = rental_income + other_income
        self.expenses = taxes + renovations + mortgage + repairs + vacancy + insurance + hoa + other_expenses 
        self.cashoncash = downpayment + closing_costs + other_purchase_costs

    def TotalMonthlyIncome(self):
        rental_income = int(input("Enter the annual rental income."))
        other_income = int(input("Enter any other income, if applicable."))

        TMI = rental_income + other_income
        return TMI
    
    def TotalMonthlyExpense(self):
        renovations = int(input("Enter total cost of renovations."))
        repairs = int(input("Enter total cost of repairs."))
        taxes = int(input("Enter yearly property taxes."))
        mortgage = int(input("Enter yearly cost of mortgage."))
        vacancy = int(input("Enter yearly reserve costs for vacancy."))
        insurance = int(input("Enter yearly cost of home insurance."))
        hoa = int(input("Enter the yearly cost of HOA."))
        other_expenses = int(input("Enter total cost of other expenses, if applicable."))

        TME = taxes + renovations + mortgage + repairs + vacancy + insurance + hoa + other_expenses
        return TME
    
    def CashonCashFlow(self): 
        downpayment = int(input("Enter total cost of redownpayment."))
        closing_costs = int(input("Enter total cost of closing costs."))
        other_purchase_costs = int(input("Enter total cost of other purchase costs."))
        
        COC = downpayment + closing_costs + other_purchase_costs
        return COC

    def ROIcalculations(self): 
        TMI = self.rental_income
        TME = self.expenses
        COC = self.cashoncash

        Annual_Profits = TMI - TME
        EROI = (Annual_Profits / COC)
        PROI = EROI * 100
        return EROI
    