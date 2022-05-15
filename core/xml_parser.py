from typing import List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from core.tickers import Ticker, parse_ticker


def parse_xml(file_path: str) -> ElementTree:
    return ElementTree.parse(file_path)


def find_tags(file_path: str, tags: str | List[str]) -> List[Element]:
    if isinstance(tags, str):
        tags = [tags]
    parsed_tree = parse_xml(file_path)
    result: List[Element] = []
    for t in tags:
        result.extend(parsed_tree.iter(t))
    return result


def get_tickers(file_path: str) -> List[Ticker]:
    found_tags = find_tags(file_path, ["index", "stock", "crypto"])
    return [parse_ticker(f) for f in found_tags]
