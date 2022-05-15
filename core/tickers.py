from dataclasses import dataclass
from xml.etree.ElementTree import Element


@dataclass
class Ticker:
    name: str
    symbol: str


class Index(Ticker):
    pass


class Stock(Ticker):
    pass


class Crypto(Ticker):
    pass


def parse_ticker(element: Element) -> Ticker | None:
    named_tickers = {
        "index": Index,
        "stock": Stock,
        "crypto": Crypto,
    }
    if element.tag in named_tickers:
        name = next(element.iter("name")).text
        symb = next(element.iter("symbol")).text
        ClassTemplate = named_tickers[element.tag]
        return ClassTemplate(name, symb)
    return None
