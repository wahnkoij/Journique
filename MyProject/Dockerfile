FROM python:3.8-slim

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["./wait-for.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]