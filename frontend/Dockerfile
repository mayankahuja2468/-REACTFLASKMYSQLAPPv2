FROM node:16.9.1-alpine3.14
RUN mkdir /frontend
WORKDIR /frontend
COPY . .
RUN npm install
CMD ["npm", "start"]