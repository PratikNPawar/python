# import random package

import random                                

#defining main function

def main():                                  
    try:
        #open file name num1.txt ,where outfile is a file object/variable.
        outfile = open('num1.txt', 'w')
        print('The random integers between 0 to 100 are:')

        #Get 4 random integers from range 0 to 100. 
        for x in range (4):
            number = random.randrange(1, 100)

            # print that 4 random integers
            print(number)

            #Write that 4 random integers on file 'num1.txt'
            outfile.write(str(number) + '\n')

        #close the file    
        outfile.close()
        
    except ValueError:
        print("The integers must be in range 0 to 100")
main()        
        














