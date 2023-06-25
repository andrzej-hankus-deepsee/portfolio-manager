FROM python:3.10-slim 

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "portfolio_manager.entrypoints.api:api", "--host", "0.0.0.0", "--port", "8001", "--log-level", "trace"]