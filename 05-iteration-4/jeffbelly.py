def function1(some_input):
    for c in some_input:
        if type(c) == int:
            print(c)
        elif type(c) == str:
            print(c)
        elif type(c) == list:
            for x in c:
                if type(x) == list:
                    for y in x:
                        print(y)
                else:
                    print(x)
        else:
            print('HI')
    return ''
        

print(function1(['1', '2', ['jeff', 'tom'], ['42', ['billy', 'jason']]]))
