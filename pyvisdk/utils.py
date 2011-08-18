'''
Created on Jul 29, 2011

@author: eplaster
'''
import re

def camel_to_under(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
