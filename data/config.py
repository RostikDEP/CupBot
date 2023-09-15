import os, dotenv	
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")

if TOKEN == None:
	print("Fatal error. Check your TOKEN at .env ")
	quit()