# 24BIT105

# Recursive_Que-2

def binary(n):
    if n == 0:
        return ""
    return binary(n//2) + str(n%2)

print(binary(int(input("Enter a number: "))))
