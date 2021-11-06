FROM node:16-alpine3.11

WORKDIR /front-vue

RUN apk update
RUN apk add --update python make g++

COPY . /

RUN yarn

ENV HOST 0.0.0.0

# CMD ["yarn", "dev"]
