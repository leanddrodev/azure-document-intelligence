import os
from dotenv import load_dotenv

load_dotenv()

class Config:
 ENDPOINT = os.getenv("DOCINTELL_ENDPOINT")
 KEY = os.getenv("DOCINTELL_KEY1")
 AZURE_STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
 CONTAINER_NAME = os.getenv("STORAGE_CONTAINER_NAME")