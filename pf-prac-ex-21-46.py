#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    num_list=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.append(i)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))


'''
Write a python function to print the given number of diagonal lines of stars.
Sample input: 5
Expected output: 
* 
.* 
..* 
...* 
....* 
Note: Setting the end parameter of the print function to empty string prevents the issuing of the new line.
Example: print(".",end="") will maintain the cursor in the same line after displaying "."
'''

#PF-Tryout 22
def diagonal_stars(number):
   #start writing your code here
    for i in range(0,number):
        for j in range(i):
            print(".",end="")
        print("*")

number=6    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum+=rem
    if(temp%sum==0):
        return True
    else:
        return False


#PF-Prac-24
def find_gcd(num1,num2):
    if(num2==0): 
        return num1
    else:
        return find_gcd(num2,num1%num2)

num1=45
num2=9
print(find_gcd(num1,num2))


#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for i in word_list:
        count_list.append(len(i))
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))


#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))


#PF-Prac-27
def check_for_ten(num1,num2):
    if(num1==10 or num2==10 or num1+num2==10):
        return True
    else:
        return False
    
print(check_for_ten(10,9))


#PF-Tryout 28
def sing_99_bottles():
   for i in range(99,0,-1):
        print(i,end="")
        print(" bottles of beer on the wall, ",end="")
        print(i,end="") 
        print(" bottles of beer.")
        print("Take one down, pass it around, ",end="")
        print(int(i-1),end="")
        print(" bottles of beer on the wall.")
   
sing_99_bottles()


#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
        k=k+1
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list

    
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))

#PF-Prac-41
# Part-1
def get_edges(pollsters_stateedge_dict,state):
    result_list=[]
    for i in pollsters_stateedge_dict:
        li=[]
        li.append(i)
        if(state in pollsters_stateedge_dict[i]):
            li.append(pollsters_stateedge_dict[i][state])
        else:
            li.append(None)
        li=tuple(li)
        result_list.append(li)
    #start writing your code here
    return result_list

# Part-2
def find_pollster_states(pollsters_stateedge_dict):
    result_dict={}
    for i in pollsters_stateedge_dict:
        li=[]
        for j in pollsters_stateedge_dict[i]:
            li.append(j)
        result_dict[i]=li    
    #start writing your code here
    return result_dict

pollsters_stateedge_dict = { 
              "Gallup": { "WA": 7, "CA": 15, "UT": -30 }, 
              "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 }, 
              "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 }
             } 
state='WA'
print("Pollsters, States and its edge details:",pollsters_stateedge_dict)
print("Given State:",state)
output=get_edges(pollsters_stateedge_dict,state)
print("Pollster Edge details for the given state:", output)  

output1=find_pollster_states(pollsters_stateedge_dict)
print("Pollster and their entire state details:",output1)

#pf-prac--43

def find_promoted_vp(presidents_dict):
    li=[]
    promoted_vp_list=[]
    for i in presidents_dict:
        li.append(i["name"])
    for i in presidents_dict:
        if (i["vp"] in li):
            promoted_vp_list.append(i["vp"])
    return promoted_vp_list

def find_presidents_vp(presidents_dict,duration):
    li=[]
    promoted_vp_list=[]
    for i in presidents_dict:
        li.append(i["vp"])
    for i in presidents_dict:
        if (i["name"] in li and i["period"]==duration):
            promoted_vp_list.append(i["name"])
    return promoted_vp_list


presidents_dict=[{'name':'George Washington', 'vp':'John Adams','period':'1990-1993'}, 
                 {'name':'John Adams', 'vp':'Thomas Jefferson','period':'1994-1996'}, 
                 {'name':'Zachary Taylor', 'vp':'Millard Fillmore','period':'1997-1999'}, 
                 {'name':'Dwight D. Eisenhower', 'vp':'Richard Nixon','period':'1999-2001'}, 
                 {'name':'Richard Nixon', 'vp':'Spiro Agnew','period':'2001-2002'}, 
                 {'name':'Richard Nixon', 'vp':'Gerald Ford','period':'2002-2004'}] 

print("The president and vice president details:",presidents_dict)
output=find_promoted_vp(presidents_dict)
print("The list of vice presidents who also got promoted as presidents:",output)
duration='2001-2002'
print("The president and vice president details:",presidents_dict)
print("Given duration:",duration)
output1=find_presidents_vp(presidents_dict, duration)
print("The list of vice presidents who also got promoted as presidents in the given duration:",output1)

#pf-prac-45
def longest_common_substring(string1, string2):
    x_longest=0
    longest=0
    l=len(string1)
    for i in range(0,l):  
        for j in range(l-i,0,-1): 
            if(string1[i:j] in string2):
                if(longest<j):
                    longest=j
                    x_longest=i+j
    
    return string1[x_longest - longest: x_longest]

output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)




