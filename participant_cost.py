def participant_cost(attendees, food_per_person,transport_per_person):
    return attendees * (food_per_person + transport_per_person)


normal_attendees=participant_cost(10,800,200)
print (normal_attendees)
                                 
zero_attendees=participant_cost(0 ,800,200)
print (zero_attendees) 
                                                    

