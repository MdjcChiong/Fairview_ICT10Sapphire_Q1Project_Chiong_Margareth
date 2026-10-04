from pyscript import document

def calculate_total(event):
    total = 0
    receipt = ""

    products = [
        ("vivienne", "Vivienne Westwood T-shirt", 1500),
        ("spiderman", "Amazing Spiderman T-shirt", 450),
        ("polo", "Vintage D&C Polo", 1500),
        ("dalmatian", "Dalmatian T-shirt", 400),
        ("adidas", "Blue Adidas T-shirt", 500),
        ("batman", "Batman Graphic T-shirt", 450),
        ("cherry", "Cherry Blossoms T-shirt", 550),
        ("ren", "Ren T-shirt", 550)
    ]

    for id, name, price in products:
        item = document.querySelector(f"#{id}")

        if item.checked:
            total += price
            receipt += f"{name} - ₱{price}<br>"

    document.querySelector("#receipt").innerHTML = receipt
    document.querySelector("#subtotal").innerHTML = f"Total: ₱{total}"