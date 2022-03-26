n = 2 * 10 ** 5
with open('./tests/sample-4.in', 'w') as f:
    f.writelines('{} {}\n'.format(str(n), str(n)))
    for i in range(1, n+1):
        query = '2'
        if i % 2:
            query = '1'
        f.writelines('{} {}\n'.format(query, str(i)))
with open('./tests/sample-4.out', 'w') as f:
    pass
