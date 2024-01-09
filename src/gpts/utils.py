from openai import OpenAI
import json

client = OpenAI()

def create_file(file):
    return client.files.create(
        file=file,
        purpose="assistants"
    )
    
def list_files():
    return json.loads(client.files.list().json())