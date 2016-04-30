
# Testing SCALARS lists

Days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# This is a tuple, the values can not be modified

for day in Days:
	print (day)

# Now with some inline modifications


print "Now with some text added to the strings"
print "---------------------------------------"
print 

for day in Days:
	print ("Today is:"+day)

print "...Okay now we are going work with Dictionaries"

print "Here is one way..."

Locations = {'AMS': 'Amsterdam', 'BOS': 'Boston', 'LAX': 'Los Angeles', 'SEA': 'Seattle'}

for loc in Locations:
	print ("Location ID: "+loc+" is "+Locations[loc])
