def solution(string):
    length = len(string)
    print(string)
    ans = list(' ' * length)
    left_list = []
    for i in range(length):
        if string[i] == '(':
            left_list.append(i)
        elif string[i] == ')':
            if left_list:
                del left_list[-1]
            else:
                ans[i] = '?'
    if left_list:
        for i in left_list:
            ans[i] = 'x'
    print(''.join(ans))

if __name__ == "__main__":
    solution(input())