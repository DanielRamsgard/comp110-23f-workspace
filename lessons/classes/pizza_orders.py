from pizza import Pizza

# instantiating object constructor
my_pizza: Pizza = Pizza("medium", 5, False)

print(my_pizza.size)

print(my_pizza.toppings)

print(my_pizza.gluten_free)


print(my_pizza.price())

print(my_pizza.add_toppings(2))
print(my_pizza.toppings)

print(my_pizza.price())

new_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(10)

print(new_pizza.toppings)