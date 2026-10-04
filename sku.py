from pyscript import document

def generate_sku(event):
    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    stock = document.querySelector("#stock").value

    if stock == "":
        document.querySelector("#sku_result").innerHTML = "Please enter stock quantity."
        return

    stock = int(stock)

    sku = f"{category}{product}{stock:02d}"

    document.querySelector("#sku_result").innerHTML = f"SKU: {sku}"