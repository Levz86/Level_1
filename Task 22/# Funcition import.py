#import numpy as np

import statistics

with open( 'input.txt' ) as fin :

    text = fin.read()

f = open("out.txt", "x")

f = open("out.txt", "w")

for line in text.split('\n') :

    op, nums = line.split(':')

    op = op.strip()  

    nums = map( float, nums.strip().split(',') )

    

    if op == 'Avg' :

        f.write('\n The value of average of [1,2,3,5,6] is '+str(statistics.mean(nums)))

    

    if op == 'Min' :

        f.write('\n The value of min of [1,2,3,5,6] is '+str(min(nums)))

    

    if op == 'Max' :

        f.write('\n The value of max of [1,2,3,5,6] is '+str(max(nums)))

    

f.close()

f = open("out.txt", "r")

print(f.read())