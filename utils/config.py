import yaml, os
from dotenv import load_dotenv
load_dotenv()
def load_config(path="config.yaml"):
    with open(path) as f: return yaml.safe_load(f)
