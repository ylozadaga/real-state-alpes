FROM python:3.10

COPY notificator-requirements.txt ./
RUN pip install --no-cache-dir -r notificator-requirements.txt

COPY . .

CMD [ "python", "./src/notificator/main.py" ]
