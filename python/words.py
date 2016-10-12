import sys
from termcolor import colored,cprint
from time import time
from datetime import datetime as dt

import math

def print_MxN_matrix(m,n,color):
    
    if (m>9 or n>17):
        cprint("The screen allows to print a max matrix of 9X17","red")
        return 
    matrix = list([])
    for i in range(1,m+1):
        for j in range(1,n+1):
            matrix.append([i,j])

    print(2*"\n")
    rowbuffer=""    
    row="|"
    rowlen=0

    for i in range(0,(m*n)):
        row+=colored(str(matrix[i][0])+":"+str(matrix[i][1]),color) + "|"
        if (i in range(n-1,m*n+1,n)):
            rowlen=n*4+1
            if n>=10:
                rowlen+=n-10+1        
            rowbuffer+="-"*rowlen+"\n"
            rowbuffer+=row+"\n"
            row="|"
    rowbuffer+="-"*rowlen
    print(rowbuffer)
    
        
    
def string_replace(s,replace_with):
    '''
    function to replace a " " character in string with another character
    args
    s:string to be searched for " " and replace with <replacewith>
    replace_with: the string to be replaced with
    '''
    h=""
    for c in s:
        if c==" ":
            h+=replace_with
        else:
            h+=c
    return h

def is_uniquecharacters(s,sensitivity="CI"):

    '''
    [With Data Structure]
    function to determine if all the characters in the string are unique
    args
        s:string to search for unique characters
        sensitivity:case sensitive or insensitive search (CI or CS)
    '''
    tempstore=dict()
    if sensitivity=="CI":
        s=str(s).upper()
    for _ in s:
        if _ in tempstore.keys():
            print("One of the duplicate key is ", tempstore[_])
            return False
        else:
            tempstore[_] = _ 
    return True

def is_uc_loop(s):
    '''
    [Without Data Structure] 
    function to determine if all the characters in the string are unique
    args
        s:string to search for unique characters
        sensitivity:case sensitive or insensitive search (CI or CS)
    '''
    i=0
    j=0
    for _ in s:
        i+=1
        for a in s:
            j+=1
            if _==a and i!=j: 
                print("One of the duplicate key is ", _)
                return False  
        j=0   
    return True
    

def analyse_file(filename):
    try:
        file=open(filename,"rt")
        file_length=len(file.read())
        # file_word_count=[sum(1) for x in file.readline().split()]
        # file.seek(0)
        file_line_count=[sum(1) for x in file]
    finally:
        file.close()

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:	
            return False
    return True

def find_angle(hour,minute):
    """
    function that returns the angle between the hour and minute handle of the clock
    args
        hour
        minute
    return
    the minimum angle  between the hour and the minute handle of the clock
    """
# if hour== 12 and minute==00 :
#return 0   
    hour_angle_h = 30*int(hour)
    hour_angle_m = int(minute)/2 # for every minute, there is .5 degree displacement in hour needle
    hour_angle = hour_angle_h + hour_angle_m
    minute_angle = 6*int(minute)
    return min(360-abs(hour_angle-minute_angle),abs(hour_angle-minute_angle))
    
def fetch_words():
    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words=[]
        for line in story:
            line_words=line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
            for word in story_words:
                print(word)

def print_arg(url):
    """
    print_arg(arl)	
    Args:
        url is the thing that you want to pass
    """
    print(url)

attempt=0
time_start=time()
time_end=time()
position=0

def find(array,value):
    """
    function that binary traverse an array to find the value	
    Args:
    array, to be searched in  
    value, to be found
    returns
    the position of the found value in the array
    """	
    global attempt
    global time_start
    global time_end
    global position
    
    attempt+=1	
    length=len(array)
    mid = int(length/2)
    #print("length",length,array)
    
    if attempt==1:
        position=mid
        time_end=time()
    
    if value not in array:
        print("{0} does not exist in the list collection".format(value))
        return		 
    
    if(length==1):
        #time_end=dt.now().microsecond
        #print (array)
        # print ("attempt",attempt)
        # print("ET {0} milliseconds".format(float(time_end-time_start)/1000))
        print("value {0} is found in the position {1}".format(value,math.floor(position)))
        position=0
        attempt=0
        return array
    
    if(value<array[mid]):
        position-=mid/2;	
        # print("left {0} attempt {1}".format(attempt,position),array[:mid])
        find(array[:mid],value)
    else:
        position+=mid/2;
        # print("right {0} attempt {1}".format(attempt,position),array[mid:])
        find(array[mid:],value)
    
if __name__=="__main__":
    print_arg(sys.argv[1])