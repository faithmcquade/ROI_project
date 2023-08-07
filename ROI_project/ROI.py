class RentalProperty:
    def __init__(self, property_price, monthly_rental_income, electric_bill, water_bill, gas_bill, repairs_cost, tax, insurance, mortgage):
        self.property_price = property_price
        self.monthly_rental_income = monthly_rental_income
        self.electric_bill = electric_bill
        self.water_bill = water_bill
        self.gas_bill = gas_bill
        self.repairs_cost = repairs_cost
        self.tax = tax
        self.insurance = insurance
        self.mortgage = mortgage

    def calculate_cash_flow(self):
        total_monthly_expenses = self.electric_bill + self.water_bill + self.gas_bill + self.repairs_cost + self.tax + self.insurance + self.mortgage
        cash_flow = self.monthly_rental_income - total_monthly_expenses
        return cash_flow

    def calculate_roi(self, down_payment):
        annual_cash_flow = self.calculate_cash_flow() * 12
        total_investment = self.property_price - down_payment
        roi = (annual_cash_flow / total_investment) * 100
        return roi

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer or float.")

def main():
    print("Welcome to Bigger Pockets Rental Property ROI Calculator!")
    
    property_price = get_numeric_input("Enter the property price: $")
    down_payment = get_numeric_input("Enter the down payment amount: $")
    monthly_rental_income = get_numeric_input("Enter the monthly rental income: $")
    
    electric_bill = get_numeric_input("Enter the monthly electric bill cost: $")
    water_bill = get_numeric_input("Enter the monthly water bill cost: $")
    gas_bill = get_numeric_input("Enter the monthly gas bill cost: $")
    repairs_cost = get_numeric_input("Enter the monthly repairs cost: $")
    tax = get_numeric_input("Enter the monthly property tax cost: $")
    insurance = get_numeric_input("Enter the monthly insurance cost: $")
    mortgage = get_numeric_input("Enter the monthly mortgage cost: $")

    property_calculator = RentalProperty(property_price, monthly_rental_income, electric_bill, water_bill, gas_bill, repairs_cost, tax, insurance, mortgage)
    total_monthly_expenses = electric_bill + water_bill + gas_bill + repairs_cost + tax + insurance + mortgage
    monthly_cash_flow = property_calculator.calculate_cash_flow()

    print(f"Your monthly expenses total is: ${total_monthly_expenses:.2f}")
    print(f"Your monthly cash flow is: ${monthly_cash_flow:.2f}")
    
    roi = property_calculator.calculate_roi(down_payment)
    print(f"Your rental property's ROI is: {roi:.2f}%")

if __name__ == "__main__":
    main()