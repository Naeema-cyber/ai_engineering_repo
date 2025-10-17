#5. Modify tuple indirectly 

item1 = input("Enter an item: ")
item2 = input("Enter another item: ")
item3 = input("Enter another item: ")

item_list = (item1, item2, item3)
print(item_list)

new_item_1 = input("Enter a new item: ")
new_item_2 = input("Enter another item: ")


new_list = (new_item_1, new_item_2)

total_list = (new_list + item_list)
final_list = ",".join(total_list)
print(final_list)