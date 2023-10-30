def TotalMonthlyIncome(self):
            while True:
                rental_income = int(input("Enter the annual rental income."))
                valid_number = 0
                if rental_income < 0:
                    print("Please enter a 0 or a valid number.")
                elif rental_income != valid_number: 
                    print("Please enter a valid number.")
                else: 
                    return rental_income