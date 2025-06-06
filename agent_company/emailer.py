import os
import smtplib
from email.message import EmailMessage
from typing import Optional


class Emailer:
    def __init__(self,
                 smtp_server: str,
                 smtp_port: int,
                 username: str,
                 password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_address: str, subject: str, body: str):
        msg = EmailMessage()
        msg["From"] = self.username
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.username, self.password)
            server.send_message(msg)


def send_mail(to: str, subject: str, body: str,
              server: Optional[str] = None,
              port: Optional[int] = None,
              username: Optional[str] = None,
              password: Optional[str] = None):
    server = server or os.getenv("SMTP_SERVER")
    port = int(port or os.getenv("SMTP_PORT", "465"))
    username = username or os.getenv("SMTP_USERNAME")
    password = password or os.getenv("SMTP_PASSWORD")

    emailer = Emailer(server, port, username, password)
    emailer.send_email(to, subject, body)
