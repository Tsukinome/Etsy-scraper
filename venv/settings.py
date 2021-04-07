from dotenv import load_dotenv
import os

load_dotenv()

db = os.getenv("DB")
user = os.getenv("USER")
pas = os.getenv("PASSWORD")
host = os.getenv("HOST")
