FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get update && apt-get install -y wget unzip

RUN mkdir /code/models

RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1aqG_JdJslxw1R8OcFpLjgMYNcjKtCBcg' -O /code/models/1.zip
   
RUN unzip /code/models/1.zip -d /code/models/

COPY . .

EXPOSE 7860

CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]