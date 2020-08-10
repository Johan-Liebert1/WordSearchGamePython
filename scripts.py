lst = [i for i in range(1,11)]

for i in lst:
    if i % 2 == 0: 
        print(f'Inside first if, i = {i}')

    if i % 5 == 0:
        print(f'Inside second if, i = {i}')

    else:
        print(f'Inside else, i = {i}')



            