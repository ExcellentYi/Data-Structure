# def append_at_begining(x,L):
#     return [x + element for element in L]

# def bit_string(n):
#     if n == 0: return []
#     if n == 1: return ["0", "1"]
#     else:
#         return (append_at_begining("0",bit_string(n-1))+
#                 append_at_begining("1",bit_string(n-1)))

# print(bit_string(3))


'''
Alternative Approach
'''
def bit_string(n):
    if n == 0: return []
    if n == 1: return ['0','1']
    return [digit + bitString for digit in bit_string(1) 
            for bitString in bit_string(n-1)]

print(bit_string(3))

# x = '0'
# L = ['0','1','00']
# c =  [x+ele for ele in L]
# print(c)
# print('0'+'01')
# print(['0','1']+['2','3'])

# L1 = ['1','2']
# L2 = ['a','b']
# L3 = ['A','B']

# C = [num + low + up for num in L1 
#             for low in L2
#             for up in L3]
# print(C)