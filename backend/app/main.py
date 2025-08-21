from fastapi import FastAPI

app = FastAPI(title='BigCap Tracker API')

@app.get('/health')
def health():
    return {'status' : 'ok'}