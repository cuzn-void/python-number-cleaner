import numbers
import pandas as pd
import numpy as np
import re

def Clean(phoneNumber):
    
    """Enter a Phone Number to Clean""" 

    # Removal of Non-Numeric Characters
    x = re.findall("\d", numbers)

    # Add Zero in the Start If Zero is not Present
    if x[0] != '0':
        x.insert(0, '0')

    # Error Raised if Phone Number Length Is Greater Then 10
    if len(x) != 10:
        raise ValueError('Incorrect Length For Phone Number')
        
    string = "".join(x)

    return (string)
