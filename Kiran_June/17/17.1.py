#first way to like import
# import function_def
# #function_def.add()#error in this
# function_def.sub()

#2nd way to import
from function_def import sub,add
sub()
add()

from function_def import * # star means all 
sub()
add()