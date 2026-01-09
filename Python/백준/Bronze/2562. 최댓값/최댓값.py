numbers = []
for i in range(9):
    numbers.append(int(input())) # 한줄에 하나 
max_value = max(numbers) 
max_index = numbers.index(max_value) + 1 

print(max_value)
print(max_index)

'''
이렇게 풀었음 .. 
def findmax_number(array):
        for i in range (len(array)):
                number=array[i]
                is_max_num=True
                for compare_number in array:
                        if number<compare_number:
                                is_max_num=False
                                break
                if is_max_num:
                        return number,i+1
              
numbers=[3,29,38,12,57,74,40,85,61]
max,index=findmax_number(numbers)
print(max)
print(index)
'''