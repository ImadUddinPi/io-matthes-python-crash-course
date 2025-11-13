def make_pizza(size, *toppings):
    """summarize the pizza making"""
    print(f"\nMaking a {size}-inch pizza with:")
    for t in toppings:
        print(f"-{t}")
