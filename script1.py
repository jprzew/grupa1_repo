from datetime import date

print('Hello world!')
print('Today is:', date.today().strftime('%d-%m-%Y'))

banach_birth = date(1892, 3, 30)
print('It is', (date.today() - banach_birth).days,
      "days from Banach's birth.")
