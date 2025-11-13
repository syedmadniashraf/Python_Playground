# write your code here
n = int(input().strip())
k = int(input().strip())

tuples_list = []
for _ in range(n):
    line = input().strip()
    nums = tuple(int(x.strip()) for x in line.split(',') if x.strip() != '')
    tuples_list.append(nums)

def digits(x):
    return 1 if x == 0 else len(str(abs(x)))

result = [t for t in tuples_list if all(digits(v) == k for v in t)]

def fmt(t):
    # single-element tuple must end with a comma (78,)
    if len(t) == 1:
        return '(' + str(t[0]) + ',)'
    else:
        return '(' + ','.join(str(x) for x in t) + ')'

print('[' + ', '.join(fmt(t) for t in result) + ']')
