"""Script calculates days and seconds from Stefan Banach's birth."""

from datetime import date

print('Hello world!!!')
print('Today is:', date.today().strftime('%d-%m-%Y'))

banach_birth = date(1892, 3, 30)
banach_days = (date.today() - banach_birth).days
print('It is', banach_days, "days from Banach's birth.")

print(f"It is {banach_days * 24 * 60 * 60:,}"
      f" seconds from Banach's birth.")
