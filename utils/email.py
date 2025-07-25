from typing import Dict
from dotenv import load_dotenv
from agents import Agent, Runner, trace, function_tool
import requests
import os

load_dotenv(override=True)
RESEND_API_KEY = os.getenv("RESEND_API_KEY")


# @function_tool
# def send_email(body: str):
#     """ Send out an email with the given body to all sales prospects via Resend """
    
    
#     from_email = "onboarding@resend.dev"  
#     to_email = "vincentbmmrtpro@gmail.com"  
    
 
#     headers = {
#         "Authorization": f"Bearer {RESEND_API_KEY}",
#         "Content-Type": "application/json"
#     }
    
#     payload = {
#         "from": f"Vincent Bommert <{from_email}>",
#         "to": [to_email],
#         "subject": "Sales email",
#         "html": f"<p>{body}</p>" 
#     }
    
#     # Send email using Resend API
#     response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
#     # Check if the request was successful
#     if response.status_code == 202:
#         return {"status": "success"}
#     else:
#         return {"status": "failure", "message": response.text}
    

@function_tool
def send_html_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send out an email with the given subject and HTML body to all sales prospects using Resend"""
    
    # Replace with your actual verified sender and target recipient
    from_email = "onboarding@resend.dev"
    to_email = "vincentbmmrtpro@gmail.com"
    
    # Get the Resend API key from environment variable
    RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
    
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "from": f"Vincent B <{from_email}>",
        "to": [to_email],
        "subject": subject,
        "html": html_body
    }
    
    response = requests.post("https://api.resend.com/emails", json=payload, headers=headers)
    
    if response.status_code == 202:
        return {"status": "success"}
    else:
        return {"status": "failure", "message": response.text}
