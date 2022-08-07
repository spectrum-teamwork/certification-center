FROM node:latest
RUN ls -al
RUN mkdir /app
WORKDIR /app
COPY webhook.js /app

# Всю поебень что ниже надо заменить на копирование проекта и первоначальную сборку
RUN pwd
RUN ls -al
RUN echo dynamic > index.html
RUN ls -al
RUN pwd

# Это запуск хука, его оставляй
ENTRYPOINT [ "node", "webhook.js"]
