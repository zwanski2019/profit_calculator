
def calculate_profit(daily_earnings, days):
    return daily_earnings * days

def main():
    print("Profit Calculator")
    daily_earnings = float(input("Enter daily earnings in USD: "))
    days = int(input("Enter number of days: "))
    profit = calculate_profit(daily_earnings, days)
    print(f"The profit in {days} days is: ${profit:.2f}")

if __name__ == "__main__":
    main()
