C_List=[1, 2, 3, 4, 5, 0, 7, 8, 9]

nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

C_List[5]=list(nums.difference(C_List)).pop()

print( C_List)
