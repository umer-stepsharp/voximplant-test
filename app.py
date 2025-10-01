from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/voicebot")
async def voicebot(request: Request):
    try:

        data = await request.json()
        user_text = data.get("text", "")

        print(f"User said: {user_text}")

        if "hello" in user_text.lower():
            reply = "Hello! Nice to meet you."
        elif "time" in user_text.lower():
            from datetime import datetime
            reply = f"The current time is {datetime.now().strftime('%H:%M:%S')}."
        else:
            reply = f"You said: {user_text}"

        return JSONResponse(content={"reply": reply})

    except Exception as e:
        print("Error in /voicebot:", e)
        return JSONResponse(
            content={"reply": "Sorry, something went wrong."},
            status_code=500
        )
