# controlla se il numero e' 7
def is7(num):
    return True if int(num) == 7 else False

def isNearly7(num):
    return True if 6.5 < num < 7.5 else False

def stringIsSeven(numStr : str):
    return True if numStr.lower() == "seven" else False

def has7(num):
    return True if "7" in str(num) else False
    
def is7Multipler(num):
    return True if num % 7 == 0 else False

def has7Items(struct):
    return True if len(struct) == 7 else False

def stringHaseSeven(string):
    return True if "seven" in (str(string)).lower else False