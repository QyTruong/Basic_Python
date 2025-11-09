# ==== list ====
fruits = ['banana', 'orange', 'mango', 'lemon']

#insert() -> chèn vào vị trí được chỉ định
fruits.insert(1, 'apple')
print(fruits)

#append() -> chèn vào sau
fruits.append('pear')
print(fruits)

#remove() -> xóa phần tử được chỉ định
fruits.remove('orange')
print(fruits)

#pop() -> lấy phần tử từ phía sau ra (mặc định)
#Nếu chỉ định tham số vd: pop(2) -> lấy phần tử tại vị trí có index là 2
fruits.pop()
print(fruits)

#sort() -> sắp xếp (mặc định: tăng dần), truyền tham số là reversed=True để giảm dần
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
