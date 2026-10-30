#calculating budget status for the event helper budget
def budget_status(budget, total):
    if total < budget :
       return "within budget"
    elif total==budget :
        return "exact budget"
    else: 
        return "over budget"
print(budget_status(16000, 15000))#within budget
print(budget_status(16000, 16000))#exact budget
print(budget_status(16000, 17000)) #over budget



"""
Component: budget_status
Returns: "Within budget" when
total <= budget, otherwise
"Over budget"
Tests: below budget, exact
budget, over budget
Issue: none

"""
