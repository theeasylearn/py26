'''
    write a program to calculate & display gross annual income, tax and net income from monthly given income as per below income tax rule 
    annual income                           Tax Rate
    Above Rs. 24,00,001	                    30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,001 to Rs. 16,00,000	    15%
    below 12,00,000                          0%
'''
monthly_income = int(input("Enter monthly income"))
#calculate annual income 
gross_income = monthly_income * 12 
tax = 0 
if gross_income>2400001: # < > <= >= == !=
    tax = (gross_income * 30) / 100
elif gross_income>2000001:
    tax = (gross_income * 25) / 100
elif gross_income>1600001:
    tax = (gross_income * 20) / 100
elif gross_income>1200001:
    tax = (gross_income * 15) / 100

#net come 
net_income = gross_income - tax 
#display gross income tax and net income
print(f"gross income = {gross_income} tax = {tax} net income = {net_income}")

    