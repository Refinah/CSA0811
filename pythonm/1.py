def add_binary( a, b):
    result= []
    carry= 0
    bit_sum=10
    max_len = max(len(a),len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    for i in range( max_len-1, -1, -1):
       max_len = int( a[i]) + int(b[i]) + carry
       result.insert( 0, str(bit_sum % 2))
       carry = bit_sum//2


    if carry:
        result.insert( 0, '1')

    return ''.join(result)
a="11"
b="1"
result=add_binary( a, b)
print(result)
