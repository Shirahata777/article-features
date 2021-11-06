FROM node:16-alpine3.11

WORKDIR /front-vue

RUN apk update

COPY . /

RUN npm rebuild
RUN npm install -g vue-cli
RUN yarn

ENV HOST 0.0.0.0

# CMD ["yarn", "dev"]
