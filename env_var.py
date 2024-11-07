from dotenv import load_dotenv
import os

import dotenv.variables



load_dotenv()  # This line brings all environment variables from .env into os.environ
print(os.environ['output_path'])
new_path= r"C:\Users\ArturSzczotarski\Videos"


with open(".env", "w") as file:
    file.write(f"output_path ={new_path}")

os.environ['output_path'] = new_path

 # This line brings all environment variables from .env into os.environ
print(os.environ['output_path'])