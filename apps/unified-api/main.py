from fastapi import FastAPI
from .src.langfuse_client.main import LangfuseClient
import time

# Initialize Langfuse Client
langfuse = LangfuseClient()

app = FastAPI()

# Middleware to automatically trace requests
@app.middleware("http")
async def add_langfuse_trace(request, call_next):
    start_time = time.time()
    trace = langfuse.trace(name=f"{request.method} {request.url.path}")
    # Capture request metadata
    trace.metadata = {
        "method": request.method,
        "path": request.url.path,
        "query_params": request.query_params,
        'headers': dict(request.headers),
    }
    try: 
        response: Response = await call_next(reqeust)
    except Exception as e:
        end_time = time.time()
        # Capture the time elapsed
        trace.end(
            end_time=end_time,
            status_code=500,
            metadata={
                "error": str(e),
                "duration": end_time - start_time,

            },
        )
        # Re-Raise the exception to propagate it
        raise 
    end_time = time.time()
    # Add metadata to the trace
    trace.metadata.update({
        "status_code": response.status_code,
        "response_headers": dict(response.headers),
        "duration": end_time - start_time,
    })

    trace.end(end_time=end_time, status_code=response.status_code)
    
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}