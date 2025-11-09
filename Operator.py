"""
    ===================== Operator (toán tử) ============================
"""
a = 1
b = 2

# Arithmetic operations (Các toán tử đại số)
total = a + b # cộng
diff = a - b # trừ
product = a * b # nhân
division = a / b # chia (kết quả là số thực)
remainder = a % b # chia lấy phần dư. Ví 5 % 2 = 1 (tức là dư 1)
floor_division = a // b # chia (kết quả được làm tròn xuống. ví 8.4 -> 8)
exponential = a ** b # a lũy thừa b (hay a mũ b)

# In ra kết quả để kiểm tra
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(floor_division)
print(exponential)

# Boolean comparison
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2 (Dấu "==" biểu thị cho dấu bằng)
print(3 != 2)    # True, because 3 is not equal to 2 (Dấu "!=" biểu thị cho không bằng hoặc khác)

# Another way comparison
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False




