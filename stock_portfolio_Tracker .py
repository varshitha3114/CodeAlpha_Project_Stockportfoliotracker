import datetime

class Stock:
    def __init__(self, name, quantity, purchase_price):
        self.name= name
        self.quantity = quantity
        self.purchase_price = purchase_price

class Stock_Portfolio_Tracker:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, stock):
        self.portfolio.append(stock)

    def remove_stock(self, name):
        for s in self.portfolio:
            if s.name == name:
                self.portfolio.remove(s)
                return
        print(str(name)+" not found in portfolio.")

    def track_performance(self):
        total_investment = 0
        for stock in self.portfolio:
            current_price = self.get_current_price(stock.name)
            investment_value = current_price * stock.quantity
            total_investment += investment_value
            print("\n")
            print(str(stock.name)+" : "+ str (stock.quantity)+  " shares \n Current Price: " +str(current_price)+"\n Investment Value: "+str(investment_value))
            print("TOTAL INVESTMENT VALUE: "+str(total_investment))

    def get_current_price(self, name):
        return 100  


portfolio = Stock_Portfolio_Tracker()

# Add stocks
portfolio.add_stock(Stock("APPLE", 10, 120))
portfolio.add_stock(Stock("MICROSOFT", 5, 200))
portfolio.add_stock(Stock("GOOGLE", 3, 1500))
portfolio.add_stock(Stock("ANDROID",8,500))

# Remove stocks
portfolio.remove_stock("ANDROID")

# Track performance
portfolio.track_performance()
