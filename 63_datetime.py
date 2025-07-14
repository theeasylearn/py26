from datetime import datetime
birth_date = input("give your birthdate in dd-mm-yyyy format")
print(birth_date)

indian_format_date = datetime.strptime(birth_date,'%d-%m-%Y')
print(indian_format_date.strftime('%A %m-%d-%Y'))