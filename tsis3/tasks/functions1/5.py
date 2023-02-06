def permutations(str):
    if len(str) == 1:
        return [str]
    ans = []
    for i, char in enumerate(str):
        new_str = str[:i] + str[i+1:]
        for j in permutations(new_str):
            ans.append(char + j)
    return ans

print(permutations(input()))