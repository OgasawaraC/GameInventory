def displayInventory(inventory):
    print('Inventory:')

    itemTotal = 0

    for i, q in inventory.items():
        itemTotal += q
        print(q, i)
    
    print("Total number of items: " + str(itemTotal))

#Part 2 - Dragon's Loot

def newItems(inventory, addedItems):
    inventory_copy = inventory.copy()
    for item in addedItems:
        inventory_copy[item] = inventory_copy.get(item, 0)+1
    
    return inventory_copy

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon scales plating', 'dragons head']

print('\nInventory before killing the dragon:\n')
displayInventory(stuff)

print('\nInventory after killing the dragon:\n')
newInv = newItems(stuff, dragonLoot)
displayInventory(newInv)