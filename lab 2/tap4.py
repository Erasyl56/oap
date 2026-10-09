price = float(input("4999: "))
quantity = int(input("6: "))
discount = float(input("8: "))

total = price * quantity
discount_sum = total * discount / 100
final_sum = total - discount_sum

print("Жалпы сома:", total)
print("Жеңілдік сомасы:", discount_sum)
print("Төленетін сома:", final_sum)