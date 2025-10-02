from crewai import Agent
from tools.currency_tool import CurrencyConverterTool

currency_analyst = Agent(
    role="currency analyst",
    goal="Provide real-time currency conversions and financial insights.",
    backstory=(
        "You are a finance expert with deep knowledge of global exchange rates. "
        "You are here to help users with currency conversion."
    ),
    tools=[CurrencyConverterTool()],
    verbose=True
)
