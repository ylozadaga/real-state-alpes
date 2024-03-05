FROM python:3.10

EXPOSE 5000/tcp

RUN apt update \
    && apt install libpq-dev -y

WORKDIR "/src"

COPY company-auditor-requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r company-auditor-requirements.txt

COPY . .

#CMD [ "flask", "--app", "./src/company_data_auditor/api", "run", "--host=0.0.0.0"]
CMD [ "uvicorn", "company_data_auditor.main:app", "--host=0.0.0.0"]
