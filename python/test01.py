from datetime import datetime
from time import perf_counter
import time
import logging

def ET(func):
    def wrapper():
        logger = logging.getLogger("ET")
        
        # logger.setLevel(logging.DEBUG)
        start=perf_counter()        
        func()
        end = perf_counter()
        logger.info( "Elapsed time of method " + str( (end-start)*1000) +  " Milliseconds " )
        logger.debug("debug code")
    return wrapper