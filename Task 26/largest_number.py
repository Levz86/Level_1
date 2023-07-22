def largest_number(first):
    #base case, list has only onw element
    if len(first) == 1:
        return first[0]
    else:
        # recursive case, calling largest number
        maximum = largest_number(first[1:])
        if first[0] > maximum:
            #if the first element is < return as maximum 
            return first[0]
        else:
            # else return max number in sublist
            return maximum
print(largest_number([1,4,5,3]))
print(largest_number([3,1,6,8,2,4,5]))