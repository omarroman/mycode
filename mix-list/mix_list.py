#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
#Print First List
print("This first item in the list (IP): " + my_list[0] )
#Print Second List
print("The second item in the list (port): " + str(my_list[1]) )
#Print Last List
print("The last item in the list (state): " + my_list[2] )
#New List
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#Print Using .Fromat method
print("When I {} into IP addresses {} or {} I am unable to ping ports {}, {}, or {}.".format(new_list[5], new_list[3], new_list[4], new_list[0], new_list[1], new_list[2]) )
