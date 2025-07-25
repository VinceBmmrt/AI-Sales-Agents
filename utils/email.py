from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
import requests
import os

load_dotenv(override=True)
RESEND_API_KEY = os.getenv("RESEND_API_KEY")


@function_tool
def send_email(body: str):
    """ Send out an email with the given body to all sales prospects via Resend """
    
    
    from_email = "onboarding@resend.dev"  
    to_email = "vincentbmmrtpro@gmail.com"  
    
 
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": f"Vincent Bommert <{from_email}>",
        "to": [to_email],
        "subject": "Sales email",
        "html": f"<p>{body}</p>" 
    }
    
    # Send email using Resend API
    response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 202:
        return {"status": "success"}
    else:
        return {"status": "failure", "message": response.text}