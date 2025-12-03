def safe_divide(numerator, denominator):
    try:
        n1 = float(numerator)
        n2 = float(denominator)
        if n2 == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        result = n1 / n2
        return f"The result of the division is {result}"
    except ValueError:
        print("Error: Please enter numeric values only.")
        
        