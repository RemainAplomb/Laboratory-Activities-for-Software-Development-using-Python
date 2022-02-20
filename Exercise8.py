"""
    NAME:  DIBANSA, RAHMANI P.
    COURSE-YEAR LEVEL-SECTION:  BSCPE 2-2
    SUBJECT:  SOFTWARE DEVELOPMENT
    PROGRAM DESCRIPTION:  A PYTHON PROGRAM THAT SORTS A LIST THROUGH
    BUCKET SORT FUNCTION
"""

# A FUNCTION THAT ARRANGES THE GIVEN LIST USING BUCKET SORT
def bucket_sort( user_input ):
    # THE VARIABLES THAT WILL BE USED.
    bs_list = user_input
    largest_element = max(bs_list)
    length = len(bs_list)
    size = largest_element/length

    # THE FUNCTION WILL CREATE A LIST OF EMPTY LISTS THE SIZE OF THE
    # NUMBER OF ELEMENTS INSIDE THE LIST bs_list.
    # THE FOR LOOP WILL DETERMINE THE WHERE THE nth( i ) ELEMENT OF
    # bs_list BELONGS IN OUR BUCKETS.
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(bs_list[i]/size)
        if j != length:
            buckets[j].append(bs_list[i])
        else:
            buckets[length - 1].append(bs_list[i])

    # USING INSERTION SORT, THE FOR LOOP WILL ARRANGE THE LISTS
    # INSIDE THE BUCKETS.
    for i in range(length):
        insertion_sort(buckets[i])

    # USING ANOTHER FOR LOOP, THE RESULT WILL BE TAKEN FROM THE BUCKETS.
    # ONCE DONE, THE FUNCTION WILL RETURN THE RESULT
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result

# THIS IS THE FUNCTION FOR INSERTION SORT
def insertion_sort(bs_list):
    # THIS FOR LOOP WILL COUNT FROM ONE UP TO THE TOTAL
    # NUMBER OF ELEMENTS IN THE inser_list
    for i in range(1, len(bs_list)):
        temp = bs_list[i]
        j = i - 1
        # WHILE J IS  IN NOT A NEGATIVE AND temp IS SMALLER
        # THAN THE ELEMENT AT INDEX j, THE LOOP WILL CONTINUE
        while (j >= 0 and temp < bs_list[j]):
            bs_list[j + 1] = bs_list[j]
            j = j - 1
        bs_list[j + 1] = temp



# HERE THE PROGRAM WILL ASK FOR THE USER'S INPUT AND PROCESS THE
# LIST GATHERED THROUGH THE bucket_sort FUNCTION. ONCE DONE, THE
# PROGRAM WILL PRINT THE RESULTS.
user_input = input( " Enter the (nonnegative) list you would like to bucket sort: " ).split()
user_input = [ int(n) for n in user_input ]
bs_list = bucket_sort( user_input )
print ( " Sorted list: " , end = "" )
print ( bs_list )
