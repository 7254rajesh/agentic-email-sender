from tools import send_email_tool, save_excel_tool

execution_log = []


def agent_loop(goal: str):
    """
    A simple autonomous agent that reasons about a goal,
    chooses actions, executes tools, and stops when done.
    """

    # --- AGENT THINKING ---
    thought = (
        "The goal requires drafting and sending an email, "
        "then saving execution details to an Excel file. "
        "I will first send the email, then store the results."
    )
    execution_log.append({"step": "THOUGHT", "detail": thought})

    # --- AGENT ACTION 1: SEND EMAIL ---
    email_result = send_email_tool(
        recipient="nimesh.bharwada@workcorex.io, rmishra3990@gmail.com",
        subject="Sample Email from Autonomous Agent",
        body=(
            "Hello,\n\n"
            "This email was drafted and sent autonomously by an "
            "agentic AI system without using Gmail APIs or browser automation.\n\n"
            "Regards,\n"
            "Autonomous Agent"
        ),
    )
    execution_log.append({"step": "ACTION", "detail": email_result})

    # --- AGENT THINKING ---
    execution_log.append(
        {
            "step": "THOUGHT",
            "detail": "The email has been sent. I should now save the execution details.",
        }
    )

    # --- AGENT ACTION 2: SAVE EXCEL ---
    excel_result = save_excel_tool(execution_log)
    execution_log.append({"step": "ACTION", "detail": excel_result})


if __name__ == "__main__":
    goal = (
        "Draft a professional sample email and send it to "
        "nimesh.bharwada@workcorex.io, then save execution details "
        "to an Excel file."
    )

    agent_loop(goal)
