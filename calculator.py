def calculator_discount(price, discount):
    if discount >= 20:
        final_price = price - (price * discount / 100)
        return final_price
    else:
        return price
    
original_price = float(input("Enter the original price of item: "))
discount_price = float(input("Enter the discount percentage: "))

final_price = calculator_discount(original_price, discount_price)

if final_price != original_price:
        print(f"The final price after applying the discount is: {final_price}")
else:
        print(f"No discount applied. The original price is: {final_price}")