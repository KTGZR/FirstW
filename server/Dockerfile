FROM node:18.0.0

ARG APP_DIR=server

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY package*.json .

RUN npm install

RUN npm install -g nodemon

COPY . .

EXPOSE 8000

CMD ["npm","start"]
