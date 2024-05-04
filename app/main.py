from fastapi import FastAPI

app = FastAPI()

import platform

print(platform.system)