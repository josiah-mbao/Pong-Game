FROM python:3.8-slim
WORKDIR /app
COPY . /app
CMD [ "python", "game.py" ]
RUN pip install --no-cache-dir pygame==2.5.2
EXPOSE 80