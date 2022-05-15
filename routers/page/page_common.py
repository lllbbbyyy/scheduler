from starlette.templating import Jinja2Templates
import json

templates = Jinja2Templates(directory="templates")

with open('config.json') as f:
    config = json.load(f)