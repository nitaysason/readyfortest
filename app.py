from aaa.bbb.samp import calc  # Exercise 1,  line 1-2(There are two files, blabla.py and samp.py, each with its own set of functions." )
from aaa.blabla import check_array, waga

def main():
    result_calc = calc(5) # Exercise 2 , line 5-12
    print(result_calc) if should_call_calc_first() else print("Error: Please call calc before waga")

    if should_call_calc_first():
        print(waga())

def should_call_calc_first():
    return True   # Change this to False to see different behavior

print(check_array([2, 3, 5])) # Exercise 3 line 14

def sort_array(arr): # Exercise 4 , line 16-22 example  1
    return sorted(arr)


my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = sort_array(my_array)
print(sorted_array)


def sort_array_in_place(arr): # Exercise 5 , line 25-32 example  2
    arr.sort()
    print(arr)
    return arr


my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort_array_in_place(my_array)

if __name__ == "__main__":
    main()