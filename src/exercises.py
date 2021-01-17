def reverse_list(input_list):
    listReversed = input_list[::-1]
    return listReversed

def count_digits(number):
    count = 0
    while(number!=0):
        number//=10
        count+=1
    return count