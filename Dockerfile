FROM python:3.9

# Set working directory (remove extra dot)
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app code
COPY . .

# Expose port
EXPOSE 5000
ARG FLASK_PORT=5000
ENV FLASK_PORT=$FLASK_PORT
EXPOSE $FLASK_PORT

# Correct CMD syntax — comma between arguments
CMD ["python", "app.py"]
