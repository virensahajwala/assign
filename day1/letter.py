#6.Write a Python program to print alphabet pattern 'A'.
#Expected Output:
 
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);


# dynamic for a
# for letter a

n=int(input("Enter row above 5:"))
result_str="";    
for row in range(0,n):    
    for column in range(0,n):     
        if (((column == 1 or column == n-2) and row != 0) or ((row == 0 or row == n/2) and (column > 1 and column < n-2))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# letter d:

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 4)) or (1<=row<=5 and column==4) ):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# dynamic:

n=int(input("Enter row above 5:"))
result_str="";    
for row in range(0,n):    
    for column in range(0,n):     
        if (column == 1 or ((row == 0 or row == n-1) and (column > 1 and column < n-3)) or (1<=row<=n-2 and column==n-3) ):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

#letter c :
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

# dynamic :

n=int(input("Enter row above 5:"))
result_str="";    
for row in range(0,n):    
    for column in range(0,n):     
        if (column == 1 or ((row == 0 or row == n-1) and (column > 1 and column < n-1)) or (row == n/2 and column > 1 and column < n-2)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

#letter g:
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if ((0<row<6 and column == 0) or ((row == 0 or (column<5 and row ==6) or (column>2 and row ==3)) and (column >1 and column < 6))
            or (row == 3 and 1<column <2 and column < 4)or ((0<row<2 or 3<=row<=5)and column==5)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);  


# dynamic:

n=int(input("Enter row above 5:"))
result_str="";    
for row in range(0,n):    
    for column in range(0,n):     
        if ((0<row<n-1 and column == 0) or ((row == 0 or (column<n-2 and row ==n-1) or (column>2 and row ==n/2)) and (column >1 and column < n-1))
            or (row == n/2 and 1<column <2 and column < n-3)or ((0<row<2 or n/2<=row<=n-2)and column==n-2)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);  

#letter l:
n=int(raw_input("enter the nnumber of stars >1"))
for i in range(1,n+1):
   if i==n :
       for j in range(1,n):
           print  "*",
       print
   else :
       print "*"

# dog years:

n=int(raw_input("enter the dog's age in human years"))

if n==1:
    print("Dog's age is 10.5")
elif n==2:
    print("dog's age is 21")
else:
    temp=n-2
    dy=temp*4+21
    print("dog's age in dog years is",dy)

#vowel:
original = raw_input('Enter a letter:')
if  original in ('a', 'e', 'i', 'o', 'u'):
    print "vowel"
else:
    print "consonant"
 


