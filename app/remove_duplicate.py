sent_set = set()
with open('./bijankhan.txt', 'r') as f:
    for line in f:
        sent_set.add(line.strip())

with open('./bijankhan.txt', 'w') as f:
    f.write('\n'.join(sent_set))