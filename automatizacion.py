import yfinance

data = yfinance.Ticker("AAPL").history(period="6mo")
cierre = data["Close"]
print(round(cierre.max(), 2))
print(round(cierre.min(), 2))
print(round(cierre.mean(), 2))  
cierre.plot()

