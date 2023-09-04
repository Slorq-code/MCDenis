import dotenv

dotenv.load_dotenv()
import os  # noqa E402

import uvicorn  # noqa E402
from fastapi import FastAPI  # noqa E402

from users import app as users_app  # noqa E402
from workers import app as workers_app  # noqa E402

app = FastAPI()
app.mount("/workers", workers_app.app)
app.mount("/users", users_app.app)

if __name__ == "__main__":
    uvicorn.run("app:app", host=os.environ.get("HOST", "localhost"), port=os.environ.get("PORT", 8000))  # type: ignore
