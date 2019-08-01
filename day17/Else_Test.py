if __name__ == '__main__':
    for i in range(5):
        print(i)
        # if i == 3:
        #     break
    else:
        print('all print')

    while i > 0:
        print(i)
        i -= 1
        if i == 2:
            break
    else:
        print('all print')

    try:
        print(2 / 1)
    except ZeroDivisionError:
        # print('error')
        raise ZeroDivisionError('zero error')
    else:
        print('no error')

    print('....')
    