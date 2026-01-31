# run.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("pycells_api.main:app", reload=True)
