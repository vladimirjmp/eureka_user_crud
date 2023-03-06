# Eureka FullStack test
## Enunciado
Se le solicita implementar dos servicios: (10 pts)
* Que permite hacer un CRUD de usuarios
* Que permite autenticar y autorizar al usuario

Defina el modelo de datos y codifique, usando Java (Spring framework), los servicios utilizando todas las capas que considera necesarias; para ello el arquitecto de la empresa le entrega una arquitectura estándar de capas, la cual se recomienda utilizar en su desarrollo.

**Nota:**

<ol type="a">
  <li>Los nombres de cada capa de desarrollo son bastantes sugerentes</li>
  <li>Los servicios deben ser REST/JSON</li>
  <li>En caso no tenga muy claro la arquitectura presentada, utilice sus propias capas y fundamente que hace cada una.</li>
  <li>Se tomará en cuenta el manejo de excepciones, log, mensajes, códigos de error, optimización y limpieza del código</li>
</ol>

## Ejecución del proyecto
Para ejecutar el proyecto debe tener instalado docker en su equipo, tanto el Frontend como el Backend se encuentran en este repositorio, solo se debe ejecutar el siguiente comando:

```bash
$ make up
```

El url para el backend es: `http://localhost:8000`

El url para el frontend es: `http://localhost:4200`
