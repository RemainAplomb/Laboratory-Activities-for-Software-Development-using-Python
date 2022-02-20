"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTSA LIST THROUGH A
    BUBBLE SORT FUNCTION
"""


# THE FUNCTION FOR BUBBLE SORT
def bubble_sort ( user_input ):
    bs_list = user_input
    # THIS LOOP WILL START THE COUNT FROM THE LAST INDEX OF THE LIST
    # DOWN TO INDEX NUMBER 1
    for i in range( len( bs_list ) - 1, 0, -1):
        # THE is_finished VARIABLE INDICATES IF SWAPS ARE MADE
        # IN EACH GIVEN ITERATION
        is_finished = True
        # THIS FOR LOOP WILL COUNT FROM ZERO TO THE nth ITERATION
        # OF THE PARENT LOOP.
        for ii in range( 0, i ):
            # THIS DETECTS IF A NUMBER IS OUT OF PLACE
            if bs_list[ii] > bs_list[ ii + 1 ]:
                bs_list[ii], bs_list[ ii + 1 ] = bs_list[ ii + 1 ], bs_list[ii]
                is_finished = False
        # ONCE THERE ARE NO MORE SWAPS MADE, THE FUNCTION WILL RETURN
        if is_finished:
            return bs_list
                

# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE bubble_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the list you would like to bubble sort: " ).split()
user_input = [ int(n) for n in user_input ]
bs_list = bubble_sort( user_input )
print ( " Sorted list: " , end = "" )
print ( bs_list )
