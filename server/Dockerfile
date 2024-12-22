FROM node:18.0.0

ARG APP_DIR=server

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY package*.json .

RUN npm install

RUN npm install -g nodemon

RUN apt-get update || : && apt-get install python -y

RUN apt-get install python3-pip -y

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["npm","start"]
