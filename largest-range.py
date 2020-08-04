def get_largest(array):
    hash = {x: 0 for x in array}
    left = right = 0
    
    for number in array:
        if hash[number] == 0:
            left_pointer = number - 1
            right_pointer = number + 1
            while left_pointer in hash:
                hash[left_pointer] = 1
                left_pointer -= 1
            left_pointer += 1
            
            while right_pointer in hash:
                hash[right_pointer] = 1
                right_pointer += 1
            right_pointer -= 1

            if (right - left) <= (right_pointer - left_pointer):
                right = right_pointer
                left = left_pointer

    
    return print([left, right])
            

get_largest([40,4,41,1,1,37,36,42,15,38,2,39,0,3])