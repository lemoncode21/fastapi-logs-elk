import uvicorn
from fastapi import FastAPI
from logging_setup import LoggerSetup
import logging

# setup root logger
logger_setup = LoggerSetup()

# get logger for module
LOGGER = logging.getLogger(__name__)

def init_app():

    apps = FastAPI(
        title="Lemon code 21",
        description= "Fast API",
        version= "1.0.0"
    )


    @apps.on_event("startup")
    async def startup():
        LOGGER.info("--- Start up App ---")
        pass

    @apps.on_event("shutdown")
    async def shutdown():
        LOGGER.info("--- shutdown App ---")
        pass

    @apps.get('/')
    def home():
        return "welcome home!"
    
    from controllers import home

    apps.include_router(home.router)
    
    return apps


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)