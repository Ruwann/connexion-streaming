import asyncio
from pathlib import Path

import connexion
from starlette.responses import StreamingResponse


async def async_gen_numbers():
    for i in range(10):
        await asyncio.sleep(1)
        yield str(i)


async def streaming():
    return StreamingResponse(async_gen_numbers(), media_type="text/plain")


app = connexion.AsyncApp(__name__, specification_dir="spec/")
app.add_api("openapi.yaml")


if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", port=8080)
