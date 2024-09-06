#finance_tracker

def finance_calculator(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_income: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = monthly_net_income *12

    print('--------------------------------------------------------')
    print(f'Monthly Income: {currency}{monthly_income:,.2f}')
    print(f'Tax Rate: {tax_rate}{'%'}')
    print(f'Monthly Tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly Net Income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly Income: {currency}{yearly_income:,.2f}')
    print(f'Yearly Tax: {currency}{yearly_tax:,.2f}')
    print(f'Yearly Net Income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------------------------------------')

def main() -> None:
    Monthly_income: float = float(input("Enter your monthly income:"))
    Tax_rate: float = float(input("Enter the tax rate applicable in your country:"))
    finance_calculator(Monthly_income,Tax_rate,currency="INR ") 

   

if __name__ == '__main__':
    main()
    

