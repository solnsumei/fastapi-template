from typing import List
from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema
from src.config.mail_config import MAIL_CONFIG


mail_service = FastMail(MAIL_CONFIG)