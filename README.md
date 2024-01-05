# [BACKEND BALAK]

## Cómo Levantarlo

Para ejecutar este proyecto, sigue estos pasos:

1. **Instalación de Docker:**
   Asegúrate de tener Docker instalado.

2. **Docker levantado:**
   Asegúrate de que Docker esté en ABIERTO [MAC] windows no se .

3. **Construir la Imagen:**
   Ejecuta el siguiente comando para construir la imagen del proyecto. Si encuentras problemas de permisos, utiliza `sudo`.

   ```bash
   docker-compose build
   ```

   y ahora esto para levantarlo

   ```bash
   docker-compose up -d
   ```

   En la app de docker vas a encontrar la bd y la api levantadas

   Puedes acceder a ella en http://localhost:8000/
   Para la docu de SWAGGER puedes usar http://localhost:8000/docs
