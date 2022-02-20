"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    COUNTING SORT FUNCTION
"""

# THE counting_sort FUNCTION TAKES THE USER'S INPUTTED LIST AND THE LARGEST
# ELEMENT INSIDE THE LIST TO OPERATE SORTING THROUGH COUNTING.
def counting_sort( user_input , largest_element ):
    cs_list = user_input

    # THE FUNCTION WILL CREATE A LIST OF ZEROES THE SIZE OF LARGEST PLUS ONE.
    # THEN, THE CREATED LIST OF ZEROES WILL BE PROCESSED THROUGH THE LOOP
    # THAT INCREMENTS THE nth( i ) INDEX OF THE LIST.
    c = [0]*( largest_element + 1 )
    for i in range( len(cs_list) ):
        c[cs_list[i]] = c[ cs_list[i] ] + 1

    # DECREASE THE VALUE OF THE FIRST ELEMENT BY ONE.
    # AFTER THAT, PROCESS THE LIST THROUGH THE FOR LOOP THAT
    # WILL MARK THE ORDER OF THE SORTING BY MAKING USE OF THE
    # NUMBER OF TIME EACH INDEX APPEARED ON THE c LIST.
    c[0] = c[0] - 1
    for i in range( 1, largest_element + 1 ):
        c[i] = c[i] + c[i - 1]

    # CREATE A LIST THE SIZE OF THE USER'S INPUTTED LIST WITH EACH OF ITS
    # ELEMENT BEING NONE.
    # USING FOR LOOP, ITERATE THROUGH THE USER'S INPUTTED LIST IN REVERSE
    # ORDER AND SORT THE ELEMENTS.
    result = [None]*len( cs_list )
    #print( result )
    for i in reversed( cs_list ):
        result[c[i]] = i
        c[i] = c[i] - 1
    return result
 
# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE counting_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the list you would like to counting sort: " ).split()
user_input = [ int(n) for n in user_input ]
largest_element = max(user_input)
cs_list = counting_sort ( user_input , largest_element)
print ( " Sorted list: " , end = "" )
print ( cs_list )
