from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    """
    GET endpoint that returns a simple HTML webpage
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #333;
                margin: 0;
            }
            p {
                color: #666;
                margin-top: 10px;
            }
            .info {
                margin-top: 20px;
                font-size: 14px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 FastAPI Backend</h1>
            <p>Welcome to your FastAPI application!</p>
            <div class="info">
                <p>Running in Docker container</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
