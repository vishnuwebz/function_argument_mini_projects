# grocery calculator (mixing *args and kwargs)

def checkout(buyer, *items, **prices):
    print(f"Buyer: {buyer}")
    print(f"Items: {items}")
    total = sum(prices.values())
    print(f"Total cost: ${total}")

checkout("Vishnu", "apple", "banana", apple =30, banana =20)


"""
Buyer: Vishnu
Items: ('apple', 'banana')
Total cost: $50
"""