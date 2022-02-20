"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    MERGE SORT FUNCTION
"""

# THIS FUNCTION TAKES A THE USER'S INPUTTED LIST, A START VARIABLE THAT
# MARKS WHERE THE FUNCTION WOULD START ITS PROCESS, AND THE END VARIABLE
# THAT IS EQUAL TO THE TOTAL NUMBER OF ELEMENTS INSIDE THE USER'S INPUTTED
# LIST.
# MERGE SORT WILL START SORTING FROM THE INDEX START UP TO THE INDEX
# END - 1.
def merge_sort(user_input, start, end):
    m_list = user_input
    
    # IF THE END SUBTRACTED BY START IS NOT GREATER THAN ONE,
    # THEN THE FUNCTION WILL RETURN THE RESULT
    if end - start > 1:
        mid = ( start + end ) // 2
        merge_sort( m_list, start, mid )
        merge_sort( m_list, mid, end )
        MergeList( m_list, start, mid, end )
    return m_list


# THE MergeList FUNCTION WILL TAKING FOUR VARIABLE INPUTS, THESE ARE:
#   *list_input  : THE PRE-PROCESSED USER INPUT
#   *start : THE INDEX WHERE THE FUNCTION WILL START FURTHER PROCESSING
#            THE INPUTTED LIST.
#   *mid : THE INDEX THAT DENOTES THE MIDDLE INDEX OF THE CURRENT PROCESS
#   *end : THE INDEX THAT DENOTES THE END INDEX OF THE CURRENT PROCESS
def MergeList( list_input, start, mid, end):
    # THE VARIABLES USED IN PROCESSING THE INPUTTED LIST
    m_list = list_input
    left = m_list[ start:mid ]
    right = m_list[ mid:end ]
    i = 0   # LEFT ITERATION
    ii = 0  # RIGHT ITERATION
    s = start 

    # WHILE START VARIABLE PLUS THE LEFT ITERATION IS LESS THAN THE MID
    # VARIABKE, AND MID VARIABLE PLUS THE RIGHT ITERATION IS LESS THAN
    # THE END VARIABLE, THE LOOP WILL CONTINUE.
    while start + i < mid and mid + ii < end:
        # IF THE nth(i) ELEMENT OF LEFT VARIABLE IS LESS THAN THE
        # nth(ii) ELEMENT OF THE RIGHT VARIABLE, THEN THE LEFT ELEMENT
        # WILL BE PLUGGED INTO m_list.
        # OTHERWISE, THE RIGHT ELEMENT WILL BE PLUGGED INTO m_list.
        if left[i] <= right[ii]:
            m_list[s] = left[i]
            i = i + 1
        else:
            m_list[s] = right[ii]
            ii = ii + 1
        s = s + 1

    # THIS WILL TAKE CARE OF THE ELEMENTS THAT ARE STILL NOT PLACED AT THE
    # RIGHT INDEX/ORDER.
    if start + i < mid:
        while s < end:
            m_list[s] = left[i]
            i = i + 1
            s = s + 1
    else:
        while s < end:
            m_list[s] = right[ii]
            ii = ii + 1
            s = s + 1
 

# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE merge_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the list you would like to merge sort: " ).split()
user_input = [ int(n) for n in user_input ]
m_list = merge_sort(user_input, 0, len(user_input))
print ( " Sorted list: " , end = "" )
print ( m_list )
