import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from agentsAi.sales_agents import sales_agent1, sales_agent2, sales_agent3, sales_picker
from utils.email import send_html_email
from agents import Agent, Runner, trace
from agentsAi.email_formatter import handoffs, tools
from agentsAi.sales_manager import sales_manager
import asyncio

load_dotenv(override=True)

async def main():
    message = "Write a cold sales email"

    with trace("Parallel cold emails"):
        results = await asyncio.gather(
            Runner.run(sales_agent1, message),
            Runner.run(sales_agent2, message),
            Runner.run(sales_agent3, message),
        )

    outputs = [result.final_output for result in results]

    for output in outputs:
        print(output + "\n\n")

    emails = "Cold sales emails:\n\n".join(outputs)

    with trace("Selection from sales people"):
        best = await Runner.run(sales_picker, emails)

    print(f"Best sales email:\n{best.final_output}")

    message2 = "Send a cold sales email addressed to 'Dear CEO'"

    with trace("Sales manager"):
        result = await Runner.run(sales_manager, message2)

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    

    