from os import supports_bytes_environ
import numpy as np
import math
input = open("input.txt", "r")

sub_in = []
sub_out = []

def setup():
    inp = []
    out = []
    for each in input:
        line = each.split("\n")[0]
        iosplit = line.split(" | ")
        inp.append(iosplit[0].split(" "))
        out.append(iosplit[1].split(" "))
    #pdb; pdb.set_trace()
    return inp, out

def calculate_unique(arr):
    unique_length = [2,3,4,7]
    count = 0
    for single in arr:
        for val in single:
            for num in unique_length:
                if len(val) == num:
                    count +=1

    return count  

def code_contains(code, contain_value, all):
    #import pdb; pdb.set_trace()
    arr = [letter for letter in code]
    vals = [letter for letter in contain_value]
    count = len(contain_value)
    for letter in arr:
        if letter in vals:
            count -=1
    
    if all and count==0:
        return True
    elif not all and count!=0:
        return True
    else:
        return False

def codes_equal(x, y):
    if len(x) != len(y):
        return False
    #import pdb; pdb.set_trace()
    code1 = [letter for letter in x]
    code2 = [letter for letter in y]
    for letter1 in code1:
        match = False
        for letter2 in code2:
            if letter1 == letter2:
                match = True
        if not match:
            return False
    return True
        

def calculate_values(sub_in, sub_out):
    '''
        calculates the values for the unique digits
    '''
    code_sum = 0
    for i in range(0, len(sub_in)):
        code_arr = ["", "", "", "","", "", "", "", "", ""]
        #import pdb; pdb.set_trace()

        for code in sub_in[i]:
            if len(code) == 2:
                code_arr[1] = code
            if len(code) == 3:
                code_arr[7] = code
            if len(code) == 4:
                code_arr[4] = code
            if len(code) == 7:
                code_arr[8] = code
        # get 6 and 3, 
        # 6 is only 6letter without both 1 values
        # 3 is only 5letter with both 1 values
        for code in sub_in[i]:
            if len(code) == 6 and code_contains(code, code_arr[1], False):
                code_arr[6] = code
            if len(code) == 5 and code_contains(code, code_arr[1], True):
                code_arr[3] = code
        
        # get remaining 5letter
        # 6 will NOT contain all digits in 2
        # 6 will contain all digits in 5
        for code in sub_in[i]:
            if len(code) == 5 and code_contains(code_arr[6], code, True):
                code_arr[5] = code
            if len(code) == 5 and code_contains(code_arr[6], code, False) and code_contains(code, code_arr[1], False):
                code_arr[2] = code
            
        # get remaining 6letter
        # 0 will NOT contain all digits in 5
        # 9 will be the last one left
        for code in sub_in[i]:
            if len(code) == 6 and code_contains(code, code_arr[5], False):
                code_arr[0] = code
            if len(code) == 6 and code_contains(code, code_arr[5], True) and code_contains(code, code_arr[6], False):
                code_arr[9] = code


            
        
        # NOW CALCULATE THE OUTPUT
        output_num = []
        for code in sub_out[i]:
            for i in range(0, len(code_arr)):
                if codes_equal(code, code_arr[i]):
                    
                    output_num.append(str(i))
                    #print("code ", code, " code matched: ",  code_arr[i])
                    break
        
        print(sub_out[i], " : ", int("".join(output_num)))
        code_sum += int("".join(output_num))
    return code_sum

             


sub_in, sub_out = setup()
print("q1 number of unique values is ", calculate_unique(sub_out))
print("q2 sum of output values is ", calculate_values(sub_in, sub_out))
