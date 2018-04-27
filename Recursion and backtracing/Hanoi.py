def hanoi(n, _from = 'A',buffer = 'B',to = 'C'):
    if n == 1: 
        print('From ',_from,'--> ',to)
        return
    else:
        hanoi(n-1, _from, to, buffer) # (n-1) from source to destination 
        hanoi(1,_from,buffer,to) # nth from source to destination
        hanoi(n-1,buffer,_from,to)# (n-1) from buffer to source

hanoi(5)

