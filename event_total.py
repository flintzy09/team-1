
#calculating the participant_cost for the event helper budget.
def participant_cost(attendee, food_per_person,transport_per_person):
    cost = attendee * (food_per_person + transport_per_person)
    return cost

print(participant_cost(10, 800, 200))# Normal attendee count
print(participant_cost(0, 800, 200))# 