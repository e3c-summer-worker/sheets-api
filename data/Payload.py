from data.Size import Size
from typing import List
from pydantic import BaseModel

Row = List[str]

# Payload when a sheet uploads data to our app
class Payload(BaseModel):
    id: str # The ID of the spreadsheet
    name: str # title of the Google Spreadsheet
    columnNames: List[str]
    size: Size
    rows: List[Row]


