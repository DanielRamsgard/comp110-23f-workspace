"""Lists practice."""
a: str = "24"
b: str = a
a += "6"
print(b)
a: list[int] = [2, 4]
b: list[int] = a
a.pop(1)
print(b)