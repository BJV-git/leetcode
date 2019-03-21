# Logic: if the matrix will get updated while specifying ranges, no need of the of again finidng the max, but keeping
# the track of the overlaps

# either ways we need ot get hold of all, as we might nto be sure about what might greater number come later
# better to go with dict, i.e. 1D index to all elements, and add the thing

# space might not be gettig affected as anyways need ot use, also might save as only updated get used

# even more effecient can be of maintaining ranges
# learned: makes sense, as the min will get any ways manipulated all the time right, caz it gonna cover from beginning in
# all the operations

# imagining sqaures getting filled up with different colours



def range_add(m,n,ops):
    r_min, c_min = m,n

    for op in ops:
        r_min = min(r_min, op[0])
        c_min = min(c_min, op[1])
    return r_min*c_min

