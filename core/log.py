import sys

RED     = "\x1b[1;31m"
GREEN   = "\x1b[1;32m"
PURPLE  = "\x1b[1;34m"
CYAN    = "\x1b[1;36m"
WHITE   = "\x1b[1;37m"
RESET   = "\x1b[1;m"

def meta(message, high=True):
    if high:
        print("["+PURPLE+" Meta "+RESET+"]\t"+message)
    else:
        print("["+CYAN+" Meta "+RESET+"]\t"+message)
    
def success(message):
    print("["+GREEN+" Success "+RESET+"]\t"+message)
    
def error(message):
    print("["+RED+" Error "+RESET+"]\t"+message)
    
def warn(message):
    print("["+YELLOW+" Warning "+RESET+"]\t"+message)
