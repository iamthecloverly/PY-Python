input_list = list(input().split())
ip = input_list
output3 = []
print("Output 1:", input_list)
ip.reverse()
print("Output 2:", ip )
for i in input_list:
     output3.append(i[::-1])
print("Output 3:", output3)
output4 = sorted(output3)[::-1]
print("Output 4:", output4)
