def categorize_by_age(age):
    if 0 <= age <= 9:
        return 'Child'
    elif 10 <= age <= 19:
        return 'Teenager'
    elif 20 <= age <= 65:
        return 'Adult'
    elif 66 <= age:
        return 'Senior'
    else:
        return f'Invalid age: {age}'
