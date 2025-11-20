from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date:", current_date.strftime('%Y-%m-%d %H:%M:%S'))
    return current_date 

def calculate_future_date():
    current =  display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current + timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
     
if __name__ == '__main__':
      
    calculate_future_date()
    
