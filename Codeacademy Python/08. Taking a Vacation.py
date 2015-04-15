def hotel_cost(nights):
    return 140*nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost = 40
    if days >= 7:
        return cost*days - 50
    elif days >= 3:
        return cost*days - 20
    else:
        return cost*days
        
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
print trip_cost('Los Angeles', 5, 600)
