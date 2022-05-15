index=1000
nIndex=index+2
name ={index : 'Muntaser' , 1001 : 'Sami' , 1002 : 'khalid'}
age ={1000:'26' , 1001:'32' , 1002:'20'}
yearOfRegisteration ={1000:'2012' , 1001:'2010' , 1002:'2009'}
while 1:
    user = input('\nType agent index to view his data (type 1000 or 1001 or 1002 in the beginning)\n')
    userty=int(user)
    if (userty in name) == True:
        print('name:', name[userty], '\nage: ', age[userty], '\nyear of registeration: ', yearOfRegisteration[userty])
    else:
        print('False index, try again')
        view=input('to view available indexies enter #0\n')
        view=int(view)
        if view == 0:
            print(list(name.keys()))
        else:
            print('ERROR')
    choose=input('\nTo insert new agent type #1 To del agent type #2\n')
    choose=int(choose)
    if choose==1:
        n = input('type his name\n')
        a = input('type his age\n')
        y = input('type his year of registeration\n')
        nnIndex=nIndex+1
        name[nnIndex] = n
        age[nnIndex] = a
        yearOfRegisteration[nnIndex] = y
        nIndex=nnIndex
    elif choose==2:
        ind=input('Enter the index of the person that you want to delete his data\n')
        ind=int(ind)
        if (ind in name) == True:
            del name[ind]
            del age[ind]
            del yearOfRegisteration[ind]
        else:
            print('Incorrect index')



