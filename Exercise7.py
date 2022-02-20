"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    RADIX SORT FUNCTION
"""

# A FUNCTION THAT SORTS THE GIVEN LIST USING RADIX SORT
def radix_sort( user_input, base=10 ):
    exp = 0 # SET EXPONENT TO ZERO
    # SET rs_list EQUAL TO THE VALUE OF THE USER'S INPUTTED LIST
    # IF THE INPUTTED LIST IS EMPTY, RETURN.
    rs_list = user_input
    if rs_list == []:
        return
    
    # A FUNCTION THAT TAKES A GIVEN DIGIT AND A BASE AS ARGUEMENTS, AND
    # RETURNS A THE KEY RESULT.
    def key_factory( digit, base ):
        def key( rs_list, index ):
            return ( ( rs_list[index] // (base**digit) ) % base )
        return key
    largest_element = max(rs_list) # FIND THE LARGEST ELEMENT

    # ONCE THE VALUE OF base WITH AN EXPONENT exp IS LESS THAN OR EQUAL
    # TO THE LARGEST ELEMENT, THE LOOP WILL STOP USING COUNTING SORT
    # TO ARRANGE THE LIST.
    while base**exp <= largest_element:
        #print ( key_factor(exp, base) )
        rs_list = counting_sort( rs_list, base - 1, key_factory(exp, base) )
        exp = exp + 1
    return rs_list
 
# THE counting_sort FUNCTION TAKES THE USER'S INPUTTED LIST AND THE LARGEST
# ELEMENT INSIDE THE LIST TO OPERATE SORTING THROUGH COUNTING.
def counting_sort( rs_list, largest_element, key ):
    # THE FUNCTION WILL CREATE A LIST OF ZEROES THE SIZE OF LARGEST PLUS ONE.
    # THEN, THE CREATED LIST OF ZEROES WILL BE PROCESSED THROUGH THE LOOP
    # THAT INCREMENTS THE nth( i ) INDEX OF THE LIST.
    cs_list = rs_list
    c = [0]*(largest_element + 1)
    for i in range(len(cs_list)):
        c[key(cs_list, i)] = c[key(cs_list, i)] + 1
 
    # DECREASE THE VALUE OF THE FIRST ELEMENT BY ONE.
    # AFTER THAT, PROCESS THE LIST THROUGH THE FOR LOOP THAT
    # WILL MARK THE ORDER OF THE SORTING BY MAKING USE OF THE
    # NUMBER OF TIME EACH INDEX APPEARED ON THE c LIST.
    c[0] = c[0] - 1 
    for i in range(1, largest_element + 1):
        c[i] = c[i] + c[i - 1]

    # CREATE A LIST THE SIZE OF THE USER'S INPUTTED LIST WITH EACH OF ITS
    # ELEMENT BEING NONE.
    # USING FOR LOOP, ITERATE THROUGH THE USER'S INPUTTED LIST IN REVERSE
    # ORDER AND SORT THE ELEMENTS.
    result = [None]*len( cs_list )
    for i in range( len( cs_list ) - 1, -1, -1 ):
        result[ c[ key(cs_list, i) ] ] = cs_list[i]
        c[ key( cs_list, i ) ] = c[ key( cs_list, i ) ] - 1
    return result
 
# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE radix_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the (nonnegative) list you would like to radix sort: " ).split()
user_input = [ int(n) for n in user_input ]
rs_list = radix_sort( user_input )
print ( " Sorted list: " , end = "" )
print ( rs_list )
