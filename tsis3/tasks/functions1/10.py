def unique_list(list):
    ans = []
    for num in list:
        if num not in ans:
            ans.append(num)
    return ans 

print(unique_list(list(input())))