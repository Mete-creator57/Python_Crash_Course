# Try It Yourself (page 41)
# Guest List 3-4
guest_list = ["Mark","Joseph","John","Clark","Ratchet","Clank"]
print(f"{guest_list[0]}, you're invited to dinner!")
print(f"{guest_list[1]}, you're invited to dinner!")
print(f"{guest_list[2]}, you're invited to dinner!")
print(f"{guest_list[3]}, you're invited to dinner!")
print(f"{guest_list[4]}, you're invited to dinner!")
print(f"{guest_list[5]}, you're invited to dinner!")

# Changing Guest List 3-5
busy = guest_list.pop(3)
print(f"{busy}, can't make the dinner today. {busy} is not available today")

print(guest_list)

# More Guests 3-6
print("A new bigger table has been founded! Now, we can have more guests!")
guest_list.insert(0, "Mitchel")
guest_list.insert(4, "Grace")
guest_list.append("Phil")
print(guest_list)

# Shrinking Guest List 3-7
print("No more spaces!")
removed = f"{guest_list.pop(5)} has been removed"
print(removed)

# removing by using remove("") function
guest_list.remove("Clank")
del guest_list[0] # removing by using del statement

