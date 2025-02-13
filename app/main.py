from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def get_greetings(name: str = 'Recruto', message: str = 'Давай дружить'):
    return f'''
    <html>
        <head>
            <title>Greetings!</title>
        </head>
        <body>
            <h1>Hello {name}! {message}!</h1>
        </body>
    </html>
    '''


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)