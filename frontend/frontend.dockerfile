# Utiliza la imagen oficial de Node.js 18 como punto de partida
FROM node:18

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia el resto de los archivos del proyecto al directorio de trabajo
COPY . .

# Construye la aplicación de Next.js
RUN npm run build

# Expone el puerto en el que se ejecutará la aplicación (por defecto, el puerto 3000)
EXPOSE 3000

# Comando para iniciar la aplicación de Next.js
CMD ["npm", "start"]