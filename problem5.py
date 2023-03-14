
def solve(n):
    # initialize variables
    current = 1
    length = 1
    block_size = 1

    while n > length:
        # move to the next block of numbers
        block_size += 1
        length += block_size

        # update the current number
        current = current * 10 + block_size

    # compute the index within the block
    index_within_block = length - n

    # extract the digit at the index
    for i in range(index_within_block):
        current //= 10
    return current % 10
def solve(n):
    # initialize variables
    current = 1
    length = 1
    block_size = 1

    while n > length:
        # move to the next block of numbers
        block_size += 1
        length += block_size

        # update the current number
        current = current * 10 + block_size

    # compute the index within the block
    index_within_block = length - n

    # extract the digit at the index
    for i in range(index_within_block):
        current //= 10
    return current % 10


n = int(input("Enter a value for n: "))
result = solve(n)
print(result)
