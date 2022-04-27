# from argparse import Namespace
# import threading


# my_string = '                  foxes'
# print(my_string)
# #.lstrip() like all string methods creates and returns a new string
# my_string.lstrip()
# print(my_string)


# #.rstip removes all extra white space from the end of a string

# my_string = '               fex \t\n'
# print(my_string)
# my_string = my_string.rstrip()
# my_string


# #.string.strip() combo l and r strip
# my_string = '               fex \t\n'
# print(my_string)
# my_string = my_string.strip()
# my_string

# #.title capitalizes the first letter of every word in a string
# my_string = 'teh fox jumped'
# print(my_string.title())


# names = ['      coNNor', 'max', ' EVan ', 'JORDAN']

# fixedNames = []

# for name in names:
#     name = name.title()
#     name = name.strip()
#     fixedNames.append(name)

# print(names)
# print(fixedNames)

# #what if we wanted to modify the values in the original list 


# #     print (name.strip().title())
# # name_list.append(name.strip().title())



# # for i in range(len(names)):
# #     print(i, names[i, name[i+1])
# #     names[i] = name[i].strip().title()
# # print(names)

# nums = [4,3,2,1]

# min()
# min(nums)
# #will return min value of sa list 
# test_list = [54,32,12,3.22, 589, 23.2]
# print(test_list)
# current_min = test_list[0]
# print(current_min)
# for number in test_list:
#     if number < current_min:
#         current_min = number
# print(current_min)

# max()
# #same as min but for max



# sum()
# #only works for lists that contain numerical values, finds the sum for all values in that lis 
# sum(list_1)
# answer = 0 
# for number in list_1:
#     answer += number
# print (answer)



# sorted()

# animals = ['fox', 'cat', 'echidna']

# sorted(animals)
# sorted_animals = sorted(animals, reverse=True)

# #does not support different data types
# #but does work on strinf and numerical data
# #sorted is out of place function, meaning it does nto alter the OG
# #.sort only works for lists
# #sorted usually for tuples
# #dictionaries are pseudo ordered
# #set = is unordered, complete 



# # .sort()
# #direclty modifying original list 


# #copying a list

# animals = ['fox', 'cat', 'echidna']
# animals2 = animals[:]
# #list sliciing!
# #we can copy a portion of a list 
# #list slicing is based on index number and has
# #parametes  similar to the range function: start, stop, step
# #name_of_list[<start>:<stop>:<step>]
# print(animals, hex(id(animals)))
# print(animals2, hex(id(animals2)))


# animals = ['fox', 'cat', 'echidna', 'bear', 'dog']
# animals[1:3]
# animals[::-1] #reversed copy of the list 
# #string slicing also exists
# #strings have the same index system, so they too can be sliced



# a_string = 'fennec fox'
# print(a_string[7:])
# print(a_string[-1::-2])
# # :: is leaving one of the inputs blank, not provdiign a stop 
# #when you dont provide a value, you dont get rid of the associated :
# #quick way to make copy of portion of a list 


# #'in' keyword is operator for memborship test 
# #is this thing part of the larger thing


# animals = ['fox', 'cat', 'echidna', 'bear', 'dog']
# if 'fox' in animals:
#     print('hi')

# #code for a list memberhsip test:
# value = 'fennec'
# for animal in animals:
#     if value == animal:
#         print('true')
#         break
# else:
#     print('false')


# #'not in' keyword
# #inverse of membership test 
# #same just checking if something is NOT in the lst 


# #checking sn empy lisyt 
# empty_1 = []
# print(empty_1, type(empty_1))
# if empty_1 == []:
#     print('list is empty')
# if empty_1:
#     #eoty list has inheret value of false
#     print('list is empty.')

# #the inverse --> returning true if the list is not emoty 
# # #is the eastist of all 
# # #if <name_list>:
# # if animals:
# #     print('not empty')

# # #removing instances with a looop
# # #while. .remove

# # #i want to remoe of all instances of repeated stings from list 
# # animals =['fox', 'cat', 'fox', 'dog', 'fox', 'fox']

# # #this fdoesn't work, adjacent repeats get skipped
# # for animal in animals:
# #     if animal == 'fox':
# #     animal.remove('fox')

# # while 'fox' in animals:
# #     animals.remove('fox')

# # print(animals)



names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
#need to append


for i in range(len(names)):
    count = 0
    for name in names:
        if names[i] == name:
            count +=1
    names = names[i+1:].remove(names[i])
    print(names)
    


    #SOLUTION 
new_names=[]
for name in names:
    if name not in  new_names:
        #add to the new list if the name is not in the new list 
        new_names.append(names)
print(new_names)

#list comprehensions 


evens = []
for n in range(20):
    if n%2 == 0:
        evens.append(n)
print(evens)

# #in a list comprehension we ahve a few pieces:
# the friust a transform for the varibale
# then the countr/variavle 
 evens = x for x in range(20) if x%2 ==0]
 print(evens)


 squares = [x**2 for x in range(20)]



 names = ['      coNNor', 'max', ' EVan ', 'JORDAN']
 names2=[x.title().strip() for x in names]

 print(names2)


#operation chaninig = combining operations with compatable outputs and inputs
name = 'dave' #string
name.title() #title acceots a string as input
#.strip also accepts a string as input
#.title() returns a string


names = ('alex', 'sven', 'tyler', 'donovan', 'brandon', 'rkisten')

for name in names:
    print(name)

#in terms of being order, iterable (can loopp through), and indexed
#a tuple is the exact same as a list 
#only diff is we cant change it 
#tuples are immuntable so we annot ditctly change them 
#in practive, howeber we can covert to a list chhange that list, then covert back to tuple

# #sorted() alwatys returns a list 
# @but soyed can acccept a tuple and will return a sorted listr with the same elemtns as the ortinial tuple 
print(names)
sorted_names = tuple(sorted(names))
print(sorted_names)
print(names)

#adding values to tuple = sant be added directly 
#when init8ially defined
#create a list version of tyour tuple, append to the list 
#then tranform back to a tuple

print(names)
names=list(names)
names.append('new_student')
print(names)
names = tuple(names)
print(names)

#tuplem comprehensions arent a thing


