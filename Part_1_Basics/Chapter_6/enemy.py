
# Simple Dictionary
enemy = {"color": "red", "health": 500,"power": 300}
print('\nOriginal enemy: ')
print(enemy)

# Modifying values in it
enemy["color"] = "yellow"
enemy["health"] += 100 
enemy["power"] = 4000

print('\nModified enemy: ')
print(enemy)

# Adding New Key-Value Pairs
enemy["height"] = 181
enemy["weight"] = 65

print(enemy)

account = {}
account["points"] = 120
account["money"] = 1000

print(f"{account['money']}$ is on your account")

if account["money"] > 100:
    print('It seems you are rich. Taking some money from you...')
    account["money"] -= 200
    print(f"Now you have {account['money']}$ on your account")

print(account)

account["debt"] = 200
account['extra points'] = 100

# Removing Key-Value Pairs
del account["points"] # removing permanently
print(account)
# providing a default value in case a specified key doesn't exist
extra_points = account.pop('random thing','There is no such a key')
print(extra_points)

# removing the last item
last = account.popitem()
print(last)


