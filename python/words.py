import sys
from termcolor import colored,cprint
from time import time
from datetime import datetime as dt

import math
error_color="red"

class top_coder:
    
    def tokenize(string,tokens):
        '''
        function that takes a string and returns a list of tokens found in the string.
        args
            string: the string on which the tokens have to be parsed for
            token: list of legitimate tokens to be searched
        returns
            list of tokens found in the string
        '''
        return_tokens = list()
        max_token_size=""
        while (len(string)>0):
            for tok in tokens:
                if string[0:len(tok)]==tok and len(max_token_size)<len(tok):
                    max_token_size=tok
            if len(max_token_size)==0:
                string=string[1:]
            else:
                return_tokens.append(max_token_size)
                string=string[len(max_token_size):]
                max_token_size=""
        return return_tokens
                
        
    def picture(size,markers=[],print_color="red"):
        '''
        this function call the hex_print function and prints the hexagon grid with markers  
        '''
        k=hex.hex_print(size,markers,print_color)
        for i in k:
            print(i)
        
    def hex_print(size,markers=[],print_color="red"):
        '''
        [linear implementation]
        this function prints a diagnol hexagon grid and places the markers with in the specified hexagon
        args
        size: the n*n hexagon matrix. 
        markers: list of string with values on where the markers has to be places. For example ["00v","11h"] will place the v market on the 0,0 cell and h marker on the 1,1 cell 
        '''
        
        hex_parts=[" _","/"+colored({0},print_color)+"\\","\\_/"]

        marker=" "
        # state machine 
        hex_width=list()
        hex_height=list()

        #return result
        return_list=list()
        loops=0
        markers_hash=dict()

        # place the markers in a hash map for quick access
        for l in markers:
            loops+=1
            if(len(l)==3):
                markers_hash[l[0:1]+"-"+l[1:2]]=l[2:3]

        # seeding the state machine with initializers
        for i in range(0,size):
            loops+=1
            hex_width.append(-1*i) #state to determine which Hex part has to be placed
            hex_height.append(-1) # state to determine when to place the markers inside hex part (1)
        

        for i in range(0,size*3*len(hex_width)):
            loops+=1

            j=i%size # state for new lines
            
            if j==0:
                return_list.append("") # new line 
            
            if hex_width[j]==0:
                return_list[len(return_list)-1]+=hex_parts[0]

            elif hex_width[j]%2==1 and hex_width[j] in range(1,size*2+1,1):
                hex_height[j]+=1 # increment the row for the corresponding hex column
                
                # check if a marker has to be placed and then get the marker
                find_key= str(hex_height[j])+"-"+str(j) 
                if(find_key in markers_hash):
                    marker = markers_hash[find_key]
                
                return_list[len(return_list)-1]+=hex_parts[1].format(marker) #place the marker
                marker=" "

            elif hex_width[j]%2==0 and hex_width[j] in range(1,size*2+1,1):
                return_list[len(return_list)-1]+=hex_parts[2]
            hex_width[j]+=1    
        
            # can be improved to do this work in line
            return_list[len(return_list)-1]=return_list[len(return_list)-1].replace("//","/")
            return_list[len(return_list)-1]=return_list[len(return_list)-1].replace("\\\\","\\")
            if(len(return_list)>1):
                return_list[len(return_list)-1]=return_list[len(return_list)-1].replace(" _","_")

        # add leading space to shift the hex to right
        for last_few_rows in range(1,size):
            loops+=1
            return_list[len(return_list)-last_few_rows]="  "*(size-last_few_rows)+return_list[len(return_list)-last_few_rows]

        print (
            str("total cost : \n reading the markers " +colored({0},"white")+
            ", \n initializing the width " + colored({1},"white")+ " of the grid matrix, \n 1 loop thru the grid matrix " + colored({2},"white")+ 
            " and \n prettying the grid " + colored({3},"white") + 
            "\n = " 
            + colored({4},"white")).format(len(markers_hash),len(hex_width),size*3*len(hex_width),size-1,loops))
        return return_list

def print_MxN_matrix(m,n,color):
    
    try:
        if (m>9 or n>17):
            raise ValueError('OutofBoundMatrix')
            return 
        matrix = list([])
        for i in range(1,m+1):
            for j in range(1,n+1):
                matrix.append([i,j])

        print("\n")
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
    except ValueError as e:   
        print(colored("Incorrect input caused Error <<{0}>>:".format(e),error_color)+"The screen allows to print a max matrix of 9X17")
    except:
        print(colored("Error <<Unknown>>:",error_color)+"some error occured, most likely incorrect color")
        
    
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