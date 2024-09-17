n_item = int(input())
barangtoko = {}

for i in range(n_item):
    item, quantity = input().split()
    quantity = int(quantity)
    barangtoko[item] = quantity

n_beli = int(input())
item_beli = []


for i in range(n_beli):
    citem, cquantity = input().split()
    cquantity = int(cquantity)
    item_beli.append(citem)
    barangtoko[citem] -= cquantity

print("CHARLIE")
print(' '.join(item_beli))
print("STORAGE")

for item, quantity in barangtoko.items():
    print(f"{item} {quantity}")           
   