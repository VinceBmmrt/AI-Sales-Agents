from agents import Agent

instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

instructions3 = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

sales_agent1 = Agent(
    name="sales_agent1",
    instructions=instructions1,
    model="gpt-4o-mini"
)

sales_agent2 = Agent(
    name="sales_agent2",
    instructions=instructions2,
    model="gpt-4o-mini"
)

sales_agent3 = Agent(
    name="sales_agent3",
    instructions=instructions3,
    model="gpt-4o-mini"
)

sales_picker = Agent(
    name="sales_picker",
    instructions="Pick the best cold sales email from the given options. Reply only with the selected email.",
    model="gpt-4o-mini"
)