
def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
 
a = 16
b = 20
 

print("The gcd of 16 and 20 is : ", end="")
print(hcf(16, 20))
if a>b:
    lcm = a
else:
    lcm = b

while True:
    if lcm%a==0 and lcm%b==0:
        break
    else:
        lcm = lcm + 1

print("\nLCM =", lcm)
