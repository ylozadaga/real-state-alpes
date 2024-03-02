FROM python:3.10

EXPOSE 5000/tcp

RUN apt update \
    && apt install libpq-dev -y

COPY company-auditor-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r company-auditor-requirements.txt

COPY . .

WORKDIR "/src"

#CMD [ "flask", "--app", "./src/company_data_auditor/api", "run", "--host=0.0.0.0"]
CMD [ "uvicorn", "company_data_auditor.main:app", "--host", "localhost", "--port", "8000", "--reload"]
