# John M Flaherty HW3: Speeding Tickets

limit = int(raw_input("Enter the speed limit.\n"))
print "You entered:", limit, "MPH"

speed = int(raw_input("Enter the speed the vagrant was going.\n"))
print "You entered:", speed, "MPH"

fine = 50                 # Base amount for speeding ticket
extra = (speed-limit)*5   # Extra $5 per MPH over limit
additionalFeeSpeed = 90   # This speed and above tacks extra fine on
over90Fine = 100          # $ amount fine for reaching above number MPH

if speed <= limit:
    print "No fine."

if speed > limit:
    total = fine + extra

    if speed >= additionalFeeSpeed:
        total = total + over90Fine
        print "The fine is:", total
    else:
        print "The fine is:", total
