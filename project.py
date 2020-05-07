import numpy as np
import pytest

def index_ring(start,size,ring):
    """indexes a list as if it were a ring and returns the
    appropriate subsection of the ring as a list
    start: starting index
    size: size of subsection to be returned
    ring: list of values"""
    length = len(ring)
    list = []
    remainder = 0
    for i in range(size):
        if start + i < length:
            list.append(ring[start+i])
        else:
            list.append(ring[remainder])
            remainder+=1
    return list

def solve_ring(ring):
    """returns the highest possible total for adding and mutltipling
    integers in the ring together"""
    n = len(ring)
    #checking that the ring is a multiple of 3
    if n%3 != 0:
        print('ring needs to be multiple of 3')
        return None

    #creating an empty matrix and looping through each square in it
    #the matrix axis are starting index vs size of ring
    matrix = np.ndarray((n,int(n/3)))

    for size in range(int(n/3)):
        for index in range(n):
            matrix[index,size] = 0

            #finding the maximum value for each matrix entry
            #by looping through all possible sums and using maximum

            #looping through all options for the last 3 values deleted from ring
            for center in range(size+1):
                for right in range(size+1 - center):
                    for left in range(center+1):

                        #adding maximum sum for leftover values in the ring using
                        #already filled in matrix sums

                        subsection = index_ring(index,(size+1)*3,ring)
                        sum = subsection[left*3]*subsection[1+center*3]*subsection[2+(center+right)*3]

                        count = 0 #how many remaining integers have been passed since last deletes value

                        #if the current value is one of the last 3 deleted values
                        #adding the maximum sum for any remaining values passed
                        for sub_index in range((size+1)*3):
                            if sub_index==left*3 or sub_index==1+center*3 or sub_index==2+(center+right)*3:
                                if count != 0:
                                    if sub_index - count + index >= n:
                                        new_index = sub_index - count + index - n
                                    else:
                                        new_index = sub_index -count + index
                                    sum += matrix[new_index,int(count/3)-1]
                                count = 0

                            else:
                                count += 1

                            #checking if the current value is the last value
                            #and adding the maximum sum for any remaining values passed
                            if count != 0 and sub_index == size-4:
                                if sub_index - count + index >= n:
                                    new_index = sub_index - count + index - n
                                else:
                                    new_index = sub_index -count + index
                                sum += matrix[new_index,int(count/3)-1]

                        #updating the matrix if the current sum is greater than the exisitng sum
                        if sum > matrix[index,size]:
                            matrix[index,size] = sum

    return max(matrix[:,int(n/3)-1])


def solve_ring_test():
    """tests if the solve_ring function returns the correct values"""
    #checking ring that is not a multiple of 3
    ring = [1,2,3,4]
    assert solve_ring(ring) == None
    #checking the basecase
    ring = [1,2,3]
    assert solve_ring(ring) == 6
    #checking a simple size 6 ring
    ring = [0,1,2,3,4,5]
    assert solve_ring(ring) == 60
    #checking a simple size 9 ring
    ring = [0,1,2,3,4,5,6,7,8]
    assert solve_ring(ring) == 396
    #checking a complicated size 9 ring
    ring = [5,8,10,99,3,2,1,98,0]
    assert solve_ring(ring) == 97026


solve_ring_test()
