"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    QUICK SORT FUNCTION
"""

# THE quivk_sort FUNCTION WILL BE TAKING THE USER'S INPUTTED LIST, THE
# START INDEX, AND THE END INDEX WHICH IS EQUAL TO THE NUMBER OF ELEMENTS
# IN THE USER'S INPUTTED LIST
def quick_sort( qs_list , start, end):
    if end - start > 1:
        p = partition(qs_list, start, end)
        quick_sort(qs_list, start, p)
        quick_sort(qs_list, p + 1, end)
 

# THIS FUNCTION WILL BE PARTITIONING THE LIST USING HOARE'S PARTITION
# SCHEME.
def partition (qs_list, start, end):
    pivot = qs_list[start] # THE PIVOT ELEMENT OF THE LIST.
    i = start + 1 # ASCENDING ITERATION
    ii = end - 1 # DESCENDING ITERATION

    # A LOOP THAT WILL JUST END AFTER THE VALUE OF ASCENDING ITERATION
    # EXCEEDS THE VALUE OF THE DESCENDING ITERATION.
    while True:
        while i <= ii and qs_list[i] <= pivot:
            i = i + 1
        while i <= ii and qs_list[ii] >= pivot:
            ii = ii - 1

        # IF THE ASCENDING ITERATION IS STILL LESS THAN OR EQUAL TO
        # THE DESCENDING ITERATION, THE LOOP WILL CONTINUE THE PROCESS.
        # ELSE, THE PROGRAM WILL SWAP THE ELEMENTS AT START INDEX AND
        # THE ELEMENT AT nth DESCENDING ITERATION.
        if i <= ii:
            qs_list[i], qs_list[ii] = qs_list[ii], qs_list[i]
        else:
            qs_list[start], qs_list[ii] = qs_list[ii], qs_list[start]
            return ii
 
# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE quick_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
qs_list = input( " Enter the list you would like to quick sort: " ).split()
qs_list = [ int(n) for n in qs_list ]
quick_sort(qs_list, 0, len(qs_list))
print ( " Sorted list: " , end = "" )
print ( qs_list )
