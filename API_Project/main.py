from fastapi import FastAPI
from app.definitions import function_definitions
from app.functions import api_functions
from app.handler import OpenAIHandler

app = FastAPI()
handler = OpenAIHandler(api_functions, function_definitions)


@app.post("/query")
async def query_endpoint(query: str):
    response = handler.send_response(query)
    return {"response": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5566)
