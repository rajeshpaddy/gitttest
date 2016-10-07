import sys
from time import time
from datetime import datetime as dt
import math
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