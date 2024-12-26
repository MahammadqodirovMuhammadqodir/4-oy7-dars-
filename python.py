# 1-misol
# def short(s1, s2):
#     if len(s1) < len(s2):
#         return s1 + s2 + s1
#     else:
#         return s2 + s1 + s2

# s1 = "short"
# s2 = "longer"
# print(short(s1, s2))

# 2-misol
# def value(lst, val):
#     return val in lst

# lst = [1, 2, 3, 4, 5]
# val = 3
# print(value(lst, val))  

# 3-misol
# def mistakes(text):
#     corrections = {'5': 'S', '0': 'O', '1': 'I', '6': 'G'}
#     return ''.join(corrections.get(char, char) for char in text)

# text = "H3LL0 W0RLD"
# print(mistakes(text))  

# 4-misol
# def binary(s):
#     return ''.join('0' if int(char) < 5 else '1' for char in s)

# s = "45385593107843568"
# print(binary(s))  