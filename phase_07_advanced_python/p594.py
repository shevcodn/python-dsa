import asyncio
import httpx
import aiofiles
import json


class StockClient:
    BASE_URL = "https://query1.finance.yahoo.com"
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self):
        self.client = None
        self.portfolio = {}
        self.alerts = {}

    async def __aenter__(self):
        self.client = httpx.AsyncClient(base_url=self.BASE_URL, headers=self.HEADERS)
        return self
    
    async def __aexit__(self, *args):
        await self.client.aclose()
        self.client = None

    async def get_price(self, ticker) -> float:
        response = await self.client.get(f"/v8/finance/chart/{ticker}", timeout=5.0)
        return float(response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"])
    
    async def get_prices(self, tickers) -> dict:
        prices = await asyncio.gather(*[self.get_price(t) for t in tickers])
        return {t: p for t, p in zip(tickers, prices) if p is not None}
    
    async def add_position(self, ticker, shares, avg_price):
        self.portfolio[ticker] = {"shares": shares, "avg_price": avg_price}
        
    async def get_portfolio_value(self) -> dict:
        result = {}
        total = 0.0
        for ticker, pos in self.portfolio.items():
            current = await self.get_price(ticker)
            value = pos["shares"] * current
            pnl = (current - pos["avg_price"]) * pos["shares"]
            result[ticker] = {"shares": pos["shares"], "current": current, "value": round(value, 2), "pnl": round(pnl, 2)}
            total += value
        result["TOTAL"] = round(total, 2)
        return result
    
    async def add_alert(self, ticker, above=None, below=None):
        self.alerts[ticker] = {"above": above, "below": below}

    async def check_alerts(self):
        for ticker, alert in self.alerts.items():
            current = await self.get_price(ticker)
            if alert["above"] is not None and current > alert["above"]:
                print(f"ALERT: {ticker} ABOVE ${alert['above']} | current: ${current}")
            if alert["below"] is not None and current < alert["below"]:
                print(f"ALERT: {ticker} BELOW ${alert['below']} | current: ${current}")

    async def save_portfolio(self, filename):
        async with aiofiles.open(filename, "w") as f:
            await f.write(json.dumps(self.portfolio, indent=2))

    async def load_portfolio(self, filename):
        async with aiofiles.open(filename, "r") as f:
            content = await f.read()
            self.portfolio = json.loads(content)


async def main():
    async with StockClient() as client:
        await client.add_position("AAPL", 10, 150.0)
        await client.add_position("TSLA", 5, 300.0)
        await client.add_position("NVDA", 8, 120.0)
        portfolio = await client.get_portfolio_value()
        for ticker, data in portfolio.items():
            if ticker == "TOTAL":
                print(f"\nTotal value: ${data}")
            else:
                print(f"{ticker}: {data['shares']} shares @ ${data['current']} | value: ${data['value']} | pnl: ${data['pnl']}")
        await client.add_alert("AAPL", above=100.0)
        await client.add_alert("TSLA", below=500.0)
        await client.add_alert("NVDA", above=5000.0)
        await client.check_alerts()
        await client.save_portfolio("portfolio.json")
        await client.load_portfolio("portfolio.json")
        print("Loaded:", client.portfolio)

if __name__ == "__main__":
    asyncio.run(main())