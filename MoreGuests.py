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

