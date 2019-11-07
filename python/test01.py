from datetime import datetime
from time import perf_counter
import time
import logging

def ET(func):
    def wrapper():
        start=perf_counter()        
        func()
        end = perf_counter()
        logging.info("<<"+ str(datetime.now()) + ">>Elapsed time of method " + func.__name__ + ":" + str( (end-start)*1000) +  " Milliseconds " )
    return wrapper