from datetime import datetime

def get_days_from_today(date: str) -> int:
   
    try:
        
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        
    
        current_date = datetime.today().date()
        
       
        delta = current_date - input_date
        
        return delta.days
        
    except ValueError:
        
        print(f"Помилка: Неправильний формат дати '{date}'. Використовуйте 'РРРР-ММ-ДД'.")
        return None


print(get_days_from_today("2021-10-09"))

