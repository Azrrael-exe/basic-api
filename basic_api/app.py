import uvicorn
from datetime import datetime
from fastapi import FastAPI
import pytz

app = FastAPI()

@app.get('/datetime')
async def get_datetime():
    sao_paulo_tz = pytz.timezone('America/Sao_Paulo')
    bogota_tz = pytz.timezone('America/Bogota')
    sao_paulo_time = datetime.now(sao_paulo_tz)
    bogota_time = datetime.now(bogota_tz)
    response = {
        'Sao_Paulo': sao_paulo_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'),
        'Bogota': bogota_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app=app, port=8080, log_level="info")