ARG NODE_VERSION=20

FROM node:${NODE_VERSION}-alpine as builder

WORKDIR /app

COPY frontend/frontend-vue/package.json .
COPY frontend/frontend-vue/package-lock.json .

RUN npm install

COPY frontend/frontend-vue .

RUN npm run build

FROM nginx:1.23-alpine as production

COPY --from=builder /app/dist /usr/share/nginx/html

COPY frontend/frontend-vue/nginx.conf /etc/nginx/conf.d/default.conf

