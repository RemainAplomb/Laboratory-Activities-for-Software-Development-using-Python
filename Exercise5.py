"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    HEAP SORT FUNCTION
"""

# THE MAIN FUNCTION THAT WILL FACILITATE THE HEAP SORTING BY MAKING USE
# OF THE OTHER FUNCTIONS.
def heap_sort( hs_list ):
    build_max_heap( hs_list )

    # THIS FOR LOOP WILL REARRANGE THE ELEMENTS
    for i in range( len( hs_list ) - 1, 0, -1 ):
        hs_list[0], hs_list[i] = hs_list[i], hs_list[0]
        max_heapify( hs_list, index=0, size=i )


# THE build_max_heap FUNCTION REARRANGES THE GIVEN LIST INTO
# A LIST REPRESENTATION OF A LIST HEAP
def build_max_heap( hs_list ):
    length = len( hs_list )
    start = parent( length - 1 )

    # THIS LOOP WILL STOP ONCE THE start VARIABLE REACHES ZERO.
    while start >= 0:
        max_heapify( hs_list, index=start, size=length )
        start = start - 1


# THIS FUNCTION TAKES IN A MODIFIED LIST OF THE hs_list THAT HAS
# A LESSER SIZE THAN THE ORIGINAL hs_list
def max_heapify( hs_list, index, size ):
    l = left( index ) # THE INDEX OF THE LEFT CHILD
    r = right( index ) # THE INDEX OF THE RIGHT CHILD

    # USING THESE CONDITIONS, THE FUNCTION WILL SORT THE GIVEN LIST
    if l < size and hs_list[l] > hs_list[index]:
        largest = l
    else:
        largest = index
    if r < size and hs_list[r] > hs_list[largest]:
        largest = r
    if largest != index:
        hs_list[largest], hs_list[index] = hs_list[index], hs_list[largest]
        max_heapify( hs_list, largest, size )


# A FUNCTION THAT RETURNS THE INDEX OF THE PARENT    
def parent( i ):
    return ( i - 1 ) // 2


# A FUNCTION THAT RETURNS THE LEFT CHILD'S INDEX
def left( i ):
    return 2*i + 1


# A FUNCTION THAT RETURNS THE RIGHT CHILD'S INDEX
def right( i ):
    return 2*i + 2


 

# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE heap_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
hs_list = input( " Enter the list you would like to heap sort: " ).split()
hs_list = [ int(n) for n in hs_list ]
heap_sort(hs_list)
print ( " Sorted list: " , end = "" )
print ( hs_list )
