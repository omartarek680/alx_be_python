def safe_divide(numerator, denominator):
    try:
        n1 = float(numerator)
        n2 = float(denominator)
        result = n1/n2
        return f"The result of the division is {result}"
 
    except ZeroDivisionError:
            return f"Error: Cannot divide by zero."
    except ValueError:
        return f"Error: Please enter numeric values only."
        
        