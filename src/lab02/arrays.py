def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError("пустой список")
    min=max=nums[0]
    for x in nums:
        if x<min:
            min=x
        if x>max:
            max=x
    return(min,max)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result=[]
    for x in nums:
        if x not in result:
            result.append(x)
    for i in range(len(result)):
        for j in range(len(result)-1 -i):
            if result[j]>result[j+1]:
                result[j],result[j+1]=result[j+1],result[j]
    return result

def flatten(mat: list[list | tuple]) -> list:
    result=[]
    for row in mat:
        if not isinstance(row,(list,tuple)):
            raise TypeError("подходят только список или кортеж")
        result+=row
    return result

nums=[[1, 2], "ab"]
if __name__=="__main__":
    print(f"мин и макс\n ввод:{nums}\nвывод:{min_max(nums)}")
    print(f"уникальные по возраст\n ввод:{nums}\nвывод:{unique_sorted(nums)}")
    print(f"общий список\n ввод:{nums}\nвывод:{flatten(nums)}")