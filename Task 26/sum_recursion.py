#creating recusive function to add number
def adding(list_integer, index_num):
    #if the idex is 0 then return value
    if index_num == 0 :
        return list_integer[0]
    # add all the numbers until index
    else:
        return list_integer[0] + adding(list_integer[1:],index_num-1)
    
print (adding([1,4,3,5,12,16],4))

print(adding([4,3,1,5],1))