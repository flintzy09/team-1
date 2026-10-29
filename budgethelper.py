
#calculating the participant_cost for the event helper budget.
def participant_cost(attendee, food_per_person,transport_per_person):
    cost = attendee * (food_per_person + transport_per_person)
    return cost

print(participant_cost(10, 800, 200))# Normal attendee count
print(participant_cost(0, 800, 200))# zero attendee count


#calculating the event_total for the event helper budget.
def event_total(attendee, food_per_person, transport_per_person,venue_cost):
    total = participant_cost(attendee,food_per_person,transport_per_person)
    return total + venue_cost

print(event_total(10, 800, 200, 5000))# Normal attendee count
print(event_total(0, 800, 200, 5000))# Zero attendee count


"""
Component:event_total
Returns: It returns total + venue_cost
Test run: normal attendee count and zero attendee count
Issue: none

"""

#calculating the budget_status for the event helper budget.
def budget_status(budget, total):
    if total < budget:
        return "Within Budget"
    elif total == budget:
        return "Exact Budget"
    else:
        return "Over Budget"

print(budget_status(16000, 15000))#Within Budget
print(budget_status(16000, 16000))#Exact Budget
print(budget_status(16000, 17000))#Over Budget


# calculating the event_summary
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira, {status}" 


# summary of event_total
print(event_summary("Study Day:", 15000, "Within Budget"))
print(event_summary("Birthday :", 20000, "Over Budget"))
    
    
        

