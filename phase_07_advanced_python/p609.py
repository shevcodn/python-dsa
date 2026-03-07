import pytest
import asyncio

async def fetch_price(ticker):
    await asyncio.sleep(0.01)
    prices = {"AAPL": 250.0, "TSLA": 400.0}
    if ticker not in prices:
        raise ValueError(f"Unknown ticker: {ticker}")
    return prices[ticker]

async def fetch_all(tickers):
    return await asyncio.gather(*[fetch_price(t) for t in tickers])

@pytest.mark.asyncio
async def test_fetch_price():
    price = await fetch_price("AAPL")
    assert price == 250.0

@pytest.mark.asyncio
async def test_fetch_unknown():
    with pytest.raises(ValueError) as exc:
        await fetch_price("GOOG")

@pytest.mark.asyncio
async def test_fetch_all():
    prices = await fetch_all(["AAPL", "TSLA"])
    assert prices == [250.0, 400.0]