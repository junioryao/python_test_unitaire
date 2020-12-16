#exercise 1 
def Exercise_One():
    
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0  :
            print('ThreeFive')
        elif i%5 == 0:
            print("Five")
        elif i%3 == 0  :
            print("Three")
        else :
            print(i)



#exercise 2 find colorfull number
def Exercise_Two(number):
    
    #check if the number is positive otherwise jump out the function
    if not number > 0 :
        return 
    
    #convert the integer input into string to split it 
    # example 321 ===> ['3','2','1]
    num_list = list(str(number))
    
    #use collect to save list of numbers
    collect = [int(i) for i in num_list ] 
    
    
    # adding the multipliers elements to the list collect 
    for i in range(len(num_list)):
        if not i == len(num_list) - 1 :
            collect.append(int(num_list[i])*int(num_list[i+1]))

    Colorfull = True   
    
    # A variable to count duplicate element
    # if any element duplicate value is greater than 1, Return False  else True
    
    for i in collect:
        duplicate = 0  
        for j in collect :
            if i == j :
                duplicate +=1 
            if duplicate > 1 :
                Colorfull = False 
                break 
        
    
    #output
    return (Colorfull)
 


#exercise 3 
def Calculate(list_of_string):

    # if the input value is not  a list return false 
    if not isinstance (list_of_string,list) :
        return False 
    
    # a variable to collect the sum 
    value = 0 
    # iterrate with every element 
    for i in list_of_string :

        if isinstance(i,str): #skip if integer 
            try :
                if isinstance(int(i) , int):
                    value = value + int(i)
            except  :
                pass
    return value 


#exercise 4 
def Anagram( word1 ,List_of_word):
        
    ''' 
       # take every element, sort them to have a unique set of word 
       # example carer and racer , sorted give (acerr) for both words 
       # the goal is to sort every word then check for the duplicate 
    
    ''' 

    #sort the word which has to be checked 
    w1 =  ''.join(sorted(list(word1)))
    
    #sort the list of word 
    lw = [ ''.join(sorted(list(i))) for i in List_of_word ]
    
    
    #anagram collector 
    anagram = []  
    
    # checking the sorted elements 
    # retreive the original word through indexing 
    for i in range(len(lw)) :
        if lw[i] == w1 :
            anagram.append(List_of_word[i])

    return (anagram)



