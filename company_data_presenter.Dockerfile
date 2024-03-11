FROM python:3.10
EXPOSE 5000/tcp
RUN apt update \
    && apt install libpq-dev -y

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "flask", "--app", "./src/company_data_presenter/api", "run", "--host=0.0.0.0"]
