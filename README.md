# AI-Sales-Agents
## Description 

#### Description (FR)
Ce projet est une application d’IA spécialisée dans la génération automatisée d’e-mails commerciaux pour une entreprise SaaS dédiée à la conformité SOC2 et la préparation d’audits grâce à l’intelligence artificielle.

Le système utilise plusieurs agents IA, chacun avec un style d’écriture distinct (professionnel, humoristique, concis), pour produire plusieurs versions d’un e-mail de prospection. Ensuite, un agent « Sélectionneur » choisit la meilleure proposition. Ce mail est ensuite envoyé automatiquement via l’API Resend grâce à une fonction dédiée.

La coordination est orchestrée via un gestionnaire d’agents, avec exécution asynchrones. Le projet met en œuvre une architecture modulaire claire, séparant les agents, la logique d’envoi d’email et le contrôle principal.

#### Project Description (EN)
This project is an AI-powered application for automated cold sales email generation for ComplAI, a SaaS company focused on SOC2 compliance and audit preparation using artificial intelligence.

The system uses multiple AI agents, each with a distinct writing style (professional, humorous, concise), to generate several versions of a sales email. Then, a “picker” agent selects the best version. The chosen email is automatically sent through the Resend API using a dedicated function.

The orchestration is managed by an agent runner with asynchronous execution. The project features a clear modular architecture, separating agents, email sending logic, and the main control flow.

## Features
Three AI sales agents generating emails in different styles (professional, humorous, concise).

A picker agent that selects the best email from generated options.

Automated email sending via Resend API.

Asynchronous execution for parallel agent runs and faster results.

Modular design for easy extension with new agents or tools.

Integrated an Email Manager agent that formats email content by generating subject lines, converting text to HTML, and handling sending via a clean handoff system between agents.

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
