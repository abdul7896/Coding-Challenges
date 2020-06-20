def reverseString(my_list):
    # setting two pointers
    left_pointer = 0
    right_pointer = len(s) - 1

    # setting a while loop to swap character
    while left_pointer < right_pointer:
        # setting a temporary pointer as we will lose the value once its set
        temp = s[left_pointer]
        # swapping first and last characters using pointers
        s[left_pointer] = s[right_pointer]
        # setting right character to temporary pointer
        s[right_pointer] = temp
        # incrementing left and decrementing right pointers
        left_pointer += 1
        right_pointer -= 1

    return my_list


print(reverseString(["h", "e", "l", "l", "o"]))
