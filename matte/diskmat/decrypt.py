# for i in range(11):
#     print(f"{i}: {((1400+i)**3)%3853327}")
# # #3838632



# # Euler's Extended Algorithm (also known as Extended Euclidean Algorithm)

# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x

# # Example usage
# a = 3233
# b = 17

# gcd, x, y = extended_gcd(a, b)

# print(f"GCD of {a} and {b} is: {gcd}")
# print(f"Coefficients x and y: {x}, {y}")
# print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")

# # Modular multiplicative inverse
# if gcd == 1:
#     inverse = x % b
#     print(f"Modular multiplicative inverse of {b} modulo {a} is: {inverse}")
# else:
#     print(f"{b} does not have a modular multiplicative inverse modulo {a}")

# # print((1266**3)%3853327)
# # print((20**13)%(29*31))

# c = 1491
# d = 1083
# n = 1711

# m = pow(c, d, n)
# print(f"Den dekrypterte meldingen m er: {m}")


print((72**69)%(113))

