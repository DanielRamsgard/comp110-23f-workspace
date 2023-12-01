class Yo:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"{self.x}"
yo = Yo(3)

print(yo)