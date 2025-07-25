# AI-Sales-Agents
## Description / Description

Français :
AI-Sales-Agents est un projet d’automatisation intelligente de la création et de l’envoi d’e-mails de prospection commerciale ciblée. Le système génère plusieurs versions d’e-mails avec différents styles, sélectionne automatiquement la meilleure et l’envoie via une API dédiée.

English :
AI-Sales-Agents is a project for intelligent automation of creating and sending targeted sales outreach emails. The system generates multiple email versions with different styles, automatically selects the best one, and sends it via a dedicated API.

## Features
Three AI sales agents generating emails in different styles (professional, humorous, concise).

A picker agent that selects the best email from generated options.

Automated email sending via Resend API.

Asynchronous execution for parallel agent runs and faster results.

Modular design for easy extension with new agents or tools.

## Technologies
Python 3.12+

OpenAI GPT via openai-agents library

Environment variables management with python-dotenv

HTTP requests with requests

Email sending through Resend API

Asynchronous programming with asyncio

Agent management and tracing with openai-agents

## Installation and Usage

Clone the repository

Install dependencies: uv sync

Copy .env.example to .env and set your environment variables

By default, the sender and recipient emails in `email.py` are set to use Resend’s testing domain.  
To use your own domain or email addresses, edit the `from_email` and `to_email` fields in that file.

Run the main script: python main.py

The script will generate multiple email drafts, print them, select the best one, and send it automatically.

## Project Structure
main.py: main script orchestrating agents and email sending

agentsAi/sales_agents.py: GPT agents for email generation and selection

utils/email.py: email sending function using Resend API

.env.example: example environment variables file