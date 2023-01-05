def isPalindrome(x):
    x = str(x)
    for i in range(len(x)):
        # print(i)
        # if x[i] == x[-i]:
        #     continue
        # else:
        #     return False
        print(x[-i])
    return True


print(isPalindrome(121))
