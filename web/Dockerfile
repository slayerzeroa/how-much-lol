# Node.js 16 이미지를 베이스로 사용
FROM node:16

# 작업 디렉터리 설정
WORKDIR /app

# package.json과 package-lock.json을 컨테이너에 복사
COPY package*.json ./

# npm 패키지 설치 (의존성 충돌 무시)
RUN npm install --legacy-peer-deps

# 소스 코드를 컨테이너에 복사
COPY . .

# Next.js 애플리케이션 빌드
RUN npm run build

# Next.js 애플리케이션을 시작
CMD ["npm", "run", "start"]

# Next.js는 기본적으로 포트 3000을 사용하므로 이를 노출
EXPOSE 3000