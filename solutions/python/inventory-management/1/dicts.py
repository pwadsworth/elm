#comprehension
def create_inventory(items: list[str]) -> dict[str, int]:
    return dict(set([(i, items.count(i)) for i in items]))

def add_items(inventory, items):
    new_items = create_inventory(items)
    return {key: inventory.get(key, 0) + new_items.get(key, 0) for key in inventory | new_items}

def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    remove_items = create_inventory(items)
    return {key: max(inventory.get(key, 0) - remove_items.get(key, 0), 0) for key in inventory}

def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    inventory.pop(item, 0)
    return inventory

def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    return [(key, inventory[key]) for key in inventory if inventory[key] > 0]