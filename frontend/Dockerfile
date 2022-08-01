FROM nginx:latest

RUN apt update
RUN apt install -y npm gconf-service libasound2 libatk1.0-0\
    libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3\
    libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0\
    libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0\
    libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1\
    libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates\
    fonts-liberation libnss3 lsb-release xdg-utils wget libgbm-dev

WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

COPY . ./
RUN npm run build

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN mv dist/* /usr/share/nginx/html/

