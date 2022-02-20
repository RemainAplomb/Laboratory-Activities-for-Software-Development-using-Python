"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    INSERTION SORT FUNCTION
"""

# THIS IS THE FUNCTION FOR INSERTION SORT
def insertion_sort( user_input):
    inser_list = user_input
    # THIS FOR LOOP WILL COUNT FROM ONE UP TO THE TOTAL
    # NUMBER OF ELEMENTS IN THE inser_list
    for i in range(1, len(inser_list)):
        temp = inser_list[i]
        j = i - 1
        # WHILE J IS  IN NOT A NEGATIVE AND temp IS SMALLER
        # THAN THE ELEMENT AT INDEX j, THE LOOP WILL CONTINUE
        while j >= 0 and temp < inser_list[j]:
            inser_list[j + 1] = inser_list[j]
            j = j - 1
        inser_list[j + 1] = temp
    return inser_list
 

# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE insertion_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the list you would like to insertion sort: " ).split()
user_input = [ int(n) for n in user_input ]
inser_list = insertion_sort( user_input )
print ( " Sorted list: " , end = "" )
print ( inser_list )
