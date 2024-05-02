# từ điển ban đầu 
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Thêm key 'pocket' vào từ điển với các phần tử chỉ định
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print("sau khi thêm 'pocket' vào từ điển:", inventory)
print("-------------------")
# Sắp xếp các phần tử trong 'backpack'
inventory['backpack'].sort()
print("Sắp xếp các phần tử trong 'backpack':", inventory)
print("--------------------")
# Loại bỏ phần tử 'dagger' khỏi 'backpack'
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')
print("Loại bỏ phần tử 'dagger' khỏi 'backpack':", inventory)
print("---------------------")
# Thêm giá trị 50 vào giá trị của 'gold'
inventory['gold'] += 50
print("Thêm giá trị 50 vào giá trị của 'gold':", inventory)
print("---------------------")
# In ra từ điển sau khi đã thực hiện các thay đổi
print("ta được từ điển mới:",inventory)
