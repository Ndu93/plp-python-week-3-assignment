#qts 2
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

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

# Get input from user
try:
    original_price = float(input("Enter the original price: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display results
    if final_price < original_price:
        print(f"\nOriginal price: ${original_price:.2f}")
        print(f"Discount applied: {discount_percent}%")
        print(f"Final price: ${final_price:.2f}")
    else:
        print(f"\nNo discount applied. Price remains ${original_price:.2f}")
        print("(Discount must be 20% or higher to be applied)")
        
except ValueError:
    print("Invalid input. Please enter numeric values only.")