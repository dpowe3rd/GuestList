# Darrell S Powe III
# This is simple list based program that builds on the previous
# This is a practice exercise from  the book 'Python Crash Course' by Eric Matthes

guests = ['Frank', 'Bob', 'Doug', 'Justin']

for i in range(len(guests)):
    print('Hello ' + guests[i] + ' I am writing you all to inform you that since Zack couldn\'t make it to dinner ' +
          guests[3] + ' will be taking his place instead. I have also found a bigger dinner table, so will be inviting '
                      'more guests shortly')

guests.insert(0, 'Steve')
guests.insert(3, 'Robert')
guests.append('Gregory')

print('\n')
for i in range(len(guests)):
    print('Here are new initiations for you all, ' + guests[i] + ', I hope you all will be able to attend my birthday')

print('\n')
print('Hello again all, unfortunately my table will not be arriving in time for my birthday dinner. I will only be '
      'able to invite 2 people to dinner.')

print('\n')
while len(guests) > 2:
    print('Dear ' + guests.pop() + ', I am sorry to say that I can no longer invite you to my birthday dinner.')

print('\n')
for x in range(len(guests)):
    print('Hello ' + guests[x] + ', I am glad to still be able to invite you to my birthday dinner. I hope to see you '
                                 'there!')

while len(guests) > 0:
    del guests[0]

print('\n')
print(guests)
