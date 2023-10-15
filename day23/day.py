nums = list(map(int, list(open('in.txt').read().strip())))
for i in range(max(nums) + 1, 1_000_000 + 1):
    nums.append(i)
length = len(nums)
print(f'There are {length} cups')
def get_clockwise(idx: int) -> list:
    global nums, length
    return [
        nums[(idx + i) % length] for i in range(1, 4)
    ]

def remove_next_3(values: list) -> None:
    global nums
    for n in values:
        nums.remove(n)

def get_dest(v: int):
    global nums
    d = v - 1
    while d not in nums:
        d -= 1
        if d < 1:
            d = max(nums)
    return d

def insert_clockwise(d_idx:int, values: list) -> None:
    global nums, length
    idxs = [(d_idx + i) % length for i in range(1,4)]
    for ix, val in zip(idxs, values):
        nums.insert(ix, val)

curr_idx = 0

def print_nums(curr) -> None:
    global nums
    s = '  '.join([str(i) for i in nums])
    s = 'cups: ' + s.replace(str(curr), f'({curr})')
    print(s)

def get_after_one_clockwise() -> str:
    global nums
    idx_one = nums.index(1)
    ret = nums[idx_one:]
    for i in nums[:idx_one]:
        ret.append(i)
    ret.remove(1)
    return ''.join(map(str, ret))
print('Begin moves...')
for itt in range(10_000_000):
    if itt+1 % 1000 == 0:
        print(f'-- Move {itt+1} --') 
    curr = nums[curr_idx]
    #print_nums(curr)
    
    next_3 = get_clockwise(curr_idx)
    remove_next_3(next_3)
    next_idx = get_dest(curr)
    dest = get_dest(curr)
    dest_idx = nums.index(dest)
    #print('pick: ' + str(next_3).replace('[','').replace(']', ''))
    #print('dest: ' + str(dest))
    
    insert_clockwise(dest_idx, next_3)
    #print()
    curr_idx = (nums.index(curr) + 1) % length
#print(get_after_one_clockwise())
idx_one = nums.index(1)

print(f'Next val: {nums[(idx_one + 1) % 1_000_000]}')
print(f'Next2val: {nums[(idx_one + 2) % 1_000_000]}')