

"""
#Lists

num = [2,5,8,10]
name = ['A1','B2','C3','D4']
print(num)
print(name)


num1 = [0] * 5        #print '0' for 5 times.
print(num1)

name1= ['Pratik', 'M'] * 2
print (name1)


#Iterating over lists
num = [10,20,30,40,50]
for i in num:
    print(i)


num = [10,20,30,40,50]
len(num)


#mutable
num=[11,22,33,44,55]
print(num)
num[0]=111     #replace 11 at index 0 with 111
num[2]=333     #replace 33 at index 2 with 333
print(num)


#mutable and concatination

list1=[2,4,6,8]
list2=[1,3,5,7]
list3=list1+list2
print(list3)

#augmentation

list1 += list2
print(list2)
print(list1)


#print('slicing')

num=[2,4,6,8,10]
print(num[1:3])
print(num[0:3])
print(num[:3])
print(num[-3:])
print(num[2:5])
print(num[2:])
print(num[0:6:2])
print(num[1:6:2])




#find value with the operator


def main():
    cars=['Audi','BMW','Mustang','Aston Martin']
    search=input('Search for this car:')
    if search in cars:
        print('Found youe model')
    else:
        print('Dont find your model')

main()
       

#built in functions - append

name=['Ann','Brad','Chou']
print(name)
name.append('Eric')


name1 = []
name1.append('Aracila')
name1.append('Taniya')
name1.append('Preeti')
name1.append('M')
print(name1)


#built in functions -indexof, sort,reverse, remove

num=[5,15,10,25,20]
print(num)
num1=num.index(20)
print(num1)
num.sort()
print(num)
num.reverse()
print(num)
num.remove(20)
print(num)
del num[0]
print(num)



# max value

season=['Spring','Summer','Fall','Winter']
print('Max season is:', max(season))
print(min(season))


# copying list

list1=[1,2,3,4,5]
list2=list1
print(list2)



#copy using for loop

list1=[10,20,30,40,50]
print(list1)
list2 = []
for i in list1:
    list2.append(i)

print(list2)    

# another way to copy

list1=[11,22,33,44]
print(list1)
list2= [] + list1
print(list2)


#processing

def main():
    list1=[1,3,5,7]
    print(list1)
    total=0
    for value in list1






# two dimensional list

teams =[['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3']]
print(teams)
print(teams[0])
print(teams[0] [0])




#writeline and readline
#read a file's content into a list using readline method


def main():

    infile=open('cities.txt','r')
    cities=infile.readline()
    #close the file
    infile.close()
    index=0
    while index < len(cities):
        cities[index] = cities[index].rstip('\n')
        index += 1
        print(cities)

main()





# another example of two dimensional list

import random
rows = 3
cols = 4

def main():
    values=[[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    #fill the list with random numbers

    for r in range(rows):

            for c in range(cols):
                values[r][c] = random.randint(1, 100)
    print(values)

main()
            
        
"""



    
