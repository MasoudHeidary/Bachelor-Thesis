message = "GPVTG,77.52,T,,M,0.004,N,0.008,K,A"

check_sum = 0
for char in message:
    check_sum ^= ord(char)

print(hex(check_sum))   #output 0x6