def sun_angle(time):
    #replace this for solution
    #Expecting time to respect a valid hh:mm value
    #import datetime 
    
    sunrise = 6*60
    sunset = 18*60

    t = int(time[0:2]) * 60 + int(time[3:5])


    if t < sunrise or t > sunset:
        return "I don't see the sun!"
    else:
        angle=round(180*(t-sunrise)/(sunset-sunrise),2)
        return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
   
    assert sun_angle("01:23") == "I don't see the sun!", "sun"
    assert sun_angle("07:00") == 15, "15"
    print("Coding complete? Click 'Check' to earn cool rewards!")