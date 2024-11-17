#qts 1
#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if it's 20% or higher.
    
    Args:
        price (float): The original price
        discount_percent (float): The discount percentage
        
    Returns:
        float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
 
print(calculate_discount(100, 25))  # result: 75.0 (25% discount applied)
print(calculate_discount(100, 15))  # result: 100.0 (no discount - below 20%)
print(calculate_discount(50, 20))   # result: 40.0 (20% discount applied)