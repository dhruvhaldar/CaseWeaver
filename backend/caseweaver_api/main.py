from fastapi import FastAPI
from caseweaver_api.routes import cases, chat, memory, openfoam, run, settings

app = FastAPI(title="Caseweaver API")

@app.get("/")
async def root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")

for r in [cases.router, chat.router, memory.router, openfoam.router, run.router, settings.router]:
    app.include_router(r)
