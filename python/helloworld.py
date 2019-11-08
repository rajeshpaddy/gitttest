import coloredlogs
import sys
from test01 import  ET
import logging
import logging.handlers
# coloredlogs.install()
##Usage python helloworld.py <your name>
logging.basicConfig(filename='test.log',level=logging.DEBUG, format='%(filename)s:[%(asctime)s]:%(lineno)d:%(message)s')
logger = logging.getLogger("Main")
fh = logging.FileHandler('test02.log')
sh = logging.StreamHandler(sys.stderr)
rh = logging.handlers.TimedRotatingFileHandler(filename="rotate.log",when='s')
rh.setLevel(logging.DEBUG)
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.CRITICAL)
logger.addHandler(fh)
logger.addHandler(sh)
logger.addHandler(rh)
#, format='%(levelname)s:%(message)s'
@ET
def tree():
    print ('Hello there!..enjoy your python learning')

logger.info("test")    
logger.info("test")
logger.debug("debug")
logger.critical("This is a critical message")

tree()

