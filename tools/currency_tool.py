import os
import requests
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class CurrencyConverterInput(BaseModel):
    amount: float = Field(..., description="The amount to be converted")
    from_currency: str = Field(..., description="The source currency code")
    to_currency: str = Field(..., description="The target currency code")

class CurrencyConverterTool(BaseTool):
    name: str = "currency converter tool"
    description: str = "Converts an amount from one currency to another."
    args_schema: Type[BaseModel] = CurrencyConverterInput
    api_key: str = os.getenv("EXCHANGE_RATE_API_KEY")

    def _run(self, amount: float, from_currency: str, to_currency: str) -> str:
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{from_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            return "Failed to fetch exchange rates."
        data = response.json()
        if "conversion_rates" not in data or to_currency not in data["conversion_rates"]:
            return f"Invalid currency code: {to_currency}"
        rate = data["conversion_rates"][to_currency]
        converted_amount = amount * rate
        return f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}."
