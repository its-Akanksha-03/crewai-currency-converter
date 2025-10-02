from crewai import Task
from agents.currency_agent import currency_analyst

currency_conversion_task = Task(
    description=(
        "Convert {amount} {from_currency} to {to_currency} "
        "using real-time exchange rates. "
        "Provide the equivalent amount and explain any relevant financial context."
    ),
    expected_output=(
        "A detailed response including the converted amount "
        "and additional financial insights."
    ),
    agent=currency_analyst
)
