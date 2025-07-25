import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from agentsAi.sales_agents import sales_agent1, sales_agent2, sales_agent3, sales_picker
from utils.email import send_email
from agents import Agent, Runner, trace

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

    description = "Write a cold sales email"

    tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description=description)
    tool2 = sales_agent2.as_tool(tool_name="sales_agent2", tool_description=description)
    tool3 = sales_agent3.as_tool(tool_name="sales_agent3", tool_description=description)

    tools = [tool1, tool2, tool3, send_email]

    instructions = (
        "You are a sales manager working for ComplAI. You use the tools given to you to generate cold sales emails. "
        "You never generate sales emails yourself; you always use the tools. "
        "You try all 3 sales_agent tools once before choosing the best one. "
        "You pick the single best email and use the send_email tool to send the best email (and only the best email) to the user."
    )

    sales_manager = Agent(name="Sales Manager", instructions=instructions, tools=tools, model="gpt-4o-mini")

    message2 = "Send a cold sales email addressed to 'Dear CEO'"

    with trace("Sales manager"):
        result = await Runner.run(sales_manager, message2)

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
