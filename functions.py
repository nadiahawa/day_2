# print()
# .strip()
# .title()
# min()
# max()
# list()
# str()
# functions 
#any time you see th esyntax some_name() where the parenthesis immediately follow rhe name , that is a function call
#diff between built in function and user def function is that the fiunction of of built in is pre written 
#function calls of a UDF or built in are the exat same
#just like the built in deifnicition of functriona like print9) or max sdotn do anything until the function is acalled

#funcction deinfinition
#def function_name():
from operator import truediv


def hello_world():
    hello = 'hello'
    thing = 'world'
    print(f'{hello}, {thing}!')
#run the pricess by calling the function 

#def function_name():
def hello_world(thing):
    hello = 'hello'
    print(f'{hello}, {thing}!')

    hello_world('naida')
    
    #that argument (or input or parameter) can be provded either as a literal value
    #thing can have ay value


    def addition(a,b, c,e,f):
        print(a+b+c+e+f)


    #returning values
    #the output of a function is its return value
    #a function can return nothing or it can return a large data structure/collection/object
    #it cannot return multiple seperate things that would make a generator
    #the return valye of a function is contorlled by he presence or lack of a return statemnt

    x=hello_world('dany devito')
    print(x)



    #same functino but returns tghe greetung instead of printit it 
    def hello_world_ret(thing):
        hello = 'hello, '
        return f'{hello}{thing}'
    y= hello_world_ret('danny devito'):
    print(y)

    #mistaike: treatingf rertun statemnet like the function call
#return(thing) - not proper, dont need oaranethsis on return statment
# bad: return(thing)
# good: return thing

#the return statment will end your function 
#regardless of any code that may come after the return statment
#if the return statemnt runs, fucntion ends

  def hello_world_ret(thing):
        hello = 'hello, '
        return(f'{hello}{thing}')

def scope_test():
    value = 'charlie day'
    return value


charlie = scope_test
print(charlie)



def decending_order(num):

    #niput is an integar
    #return value is also an integar
    #break my integaer in to a list of its digits
    #sort that list 
    #turn it back into an integar
     

     #break a string in a list of its characters
        num= list((str(num)))
        num.sort(reverse=True)
        return int(''.join(num))

 