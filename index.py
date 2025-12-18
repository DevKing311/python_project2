#Personal Expense Tracker (Python)
Expense ={"food": 0, "transport": 0, "rent": 0, "entertainment": 0, "others": 0}

food=float(input('Enter amount spent on food: '))
transport=float(input('Enter amount spent on transport: '))
rent=float(input('Enter amount spent on rent: '))
entertainment=float(input('Enter amount spent on entertainment: '))
others=float(input('Enter amount spent on others: '))
Expense['food']=food
Expense['transport']=transport
Expense['rent']=rent
Expense['entertainment']=entertainment
Expense['others']=others

print('PERSONAL EXPENSE REPORT\n ')
print("Food:",Expense['food'])
print("Transport:",Expense['transport'])
print("Rent:",Expense['rent'])
print("Entertainment:",Expense['entertainment'])
print("Others:",Expense['others'])

#Total_expenses= food + transport + rent + entertainment + others
Total_expenses= Expense['food'] + Expense['transport'] + Expense['rent'] + Expense['entertainment'] + Expense['others']
print("Total Expenses: ",Total_expenses)

Monthly_income= float(input('Enter your monthly income: '))
Monthly_budget= float(input('Enter your monthly monthly budget limit: '))
if Total_expenses> Monthly_budget:
    print("You have exceed your monthly limit..")
else:
     print("You have not  exceed your monthly limit..")


#PERCENTAGE OF INCOME
a_seven= 70/100*Monthly_income
a_nine= 90/100*Monthly_income

# Classify the user’s spending into one of the following 
if Total_expenses <= a_seven:
    print("Budget Status: Healthy Spending")
elif  Total_expenses > a_seven and Total_expenses <= a_nine:
    print("Budget Status: Warning Level")
else:
    print("Budget Status: Over Spending")

# Determine which expense category has the highest spending amount.
# This must be done using dictionary values and conditional logic.
if food>transport and food>rent and food>entertainment and food> others:
    print("You spent more on food",food)
elif transport>food and transport>rent and transport>entertainment and transport> others:
    print("You spent more on transport",transport)
elif rent>food and rent>transport and rent>entertainment and rent> others:
    print("You spent more on rent",rent)
elif entertainment>food and entertainment>rent and entertainment>transport and entertainment> others:
    print("You spent more on entertainment",entertainment)
elif others>food and others>rent and others>entertainment and others>transport:
    print("You spent more on others",others)
else:
    print("Multiple categories have the same highest expense")