from fastapi import FastAPI
from parser_page import get_parse_data
from typing import List

app = FastAPI()


@app.post("/parsers/title/")
def title_parser(urls: List[str]):
    return [title for title in get_parse_data(urls)]
