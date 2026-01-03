Project: Autonomous Agentic Email Sender

**Overview**
This project implements an autonomous, hands-free agentic AI system that drafts and sends an email and saves execution details to an Excel file without using Gmail APIs or browser automation.
The system operates end-to-end from a single goal and completes the task without human intervention.

**What the Agent Does**
Interprets a natural language goal
Decides required actions autonomously
Sends an email via SMTP
Saves execution trace to an Excel file
Terminates once the goal is satisfied

**Constraints Respected**
❌ No Gmail API usage
❌ No browser automation
✅ Fully autonomous execution
✅ Local execution

**Tech Stack**
Python
SMTP (email delivery)
Pandas + OpenPyXL (Excel output)

How to Run
1. Clone the repository
git clone https://github.com/7254rajesh/agentic-email-sender.git
cd agentic-email-sender

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure email credentials

Create a config.py file:

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "<your-gmail>"
SENDER_APP_PASSWORD = "<gmail-app-password>"
EXCEL_OUTPUT_PATH = "agent_output.xlsx"

5. Run the agent
python agent.py

**Output**
Email sent to the specified recipient
Excel file generated locally containing execution steps
Agentic Design Notes
Goal-driven execution (no hard-coded workflow)
Explicit reasoning and action steps
Tool-based interaction (email + file system)
Deterministic and explainable control loop

**Assumptions**
SMTP access via Gmail App Password is permitted
Successful SMTP handoff implies email delivery
Excel output acts as execution proof
