FROM python:3.10
LABEL author="m.agonf@uniandes.edu.co"
EXPOSE 5000/tcp
WORKDIR /app
RUN apt update \
    && apt install libpq-dev -y
COPY requirements.txt /app
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD [ "uvicorn", "main:app", "--host=0.0.0.0"]
