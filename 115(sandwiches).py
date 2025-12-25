#chef sells sandwiches for a living. Each sandwich is sold for 
#A
#A rupees.

#Chef also needs to buy the ingredients to make a sandwich. The sandwich buns cost 
#B
#B rupees, and the vegetables cost 
#C
#C rupees. Let us assume that there are no other costs for Chef right now.

#What is the profit Chef makes in selling one sandwich? It may be possible that the answer is negative to indicate that Chef makes a loss instead.

selling_price=1000
bun_price=200
veg_price=200
profit=0
print("the profit chef makes is",selling_price-(bun_price+veg_price))

# another way to do this is 
A, B, C = map(int, input().split())
print(A - (B + C))

# what this code does is as follows 
#step-1 input() here its 1000 200 and 200 reads one full line from the user as strig
# so input is "1000 200 200"
#still a stttring not numbers
#step-2 input().split() this splits the string into a list of strings ["1000", "200", "200"]
#step-3 map(int,["1000", "200", "200"]) this converts the list of strings into a list of integers [1000, 200, 200]
#step-4 A, B, C = [1000, 200, 200] this assigns the values to the variables A, B, C
