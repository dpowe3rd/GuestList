# Darrell S Powe III
# This is simple list based program that builds on the previous
# This is a practice exercise from  the book 'Python Crash Course' by Eric Matthes

seat = "Justin"
guests = ['Frank', 'Bob', 'Doug', 'Zack']

for i in range(len(guests)):
    print('Hello ' + guests[i] + ' I am inviting you to my birthday dinner, I hope you\'ll be able to attend')
print('\nUnfortunately, ' + guests.pop() + ' can\'t make it to dinner.')
print('So instead I will be inviting ' + str(seat) + '.')

guests.append(seat)

print('\n')
for i in range(len(guests)):
    print('Here are new initiations for you, ' + guests[i] + ' , I hope you all will be able to attend my birthday')