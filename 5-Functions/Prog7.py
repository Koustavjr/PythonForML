def sum_args(*args):
    print(args)
    print(*args)
    for i in args:
        print(i)
    print(sum(args))
    
sum_args(1,5,6,7)

    