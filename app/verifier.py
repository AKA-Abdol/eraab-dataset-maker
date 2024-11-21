ml = 0
with open('./bijankhan.txt', 'r') as f:
    for line in f:
        if len(line.strip()) > ml:
            ml = len(line.strip())
print(f'max character count is {ml}')