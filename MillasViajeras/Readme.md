*Título del Proyecto: MillasViajeras

*Despliegue 📦

- Clonar el repositorio 
- Dentro del proyecto abrir una terminal ejecutar python manage.py runserver
- Ingresar a la ruta que nos brinda el terminal.

- La pagina principal despliega:
Un panel de navegacion que contiene Inicio, Publicaciones, Ingresar ( Iniciar y Registrarse ), Acerca de.
Una vez registrado y logeado en la pagina se van habilitar tres solapas dentro de " Tu perfil ".

La primera es "Editar Perfil", donde podras hacer modificaciones a tus datos de registro.
La segunda es "Crear Publicacion", donde podras crear una publicacion. 
La tercera es "Mis Publicaciones", donde podras ver tus publicaciones, editarlas, borrarlas y eliminarlas. 


- Inicio: se muestra la pagina principal, en esta vista encontraras:
Una pequeña bienvenida a la pagina.
Y la ultima publicacion creada por nuestros usuarios de la web, siempre y cuando haya minimamente una. 
Los usuarios registrados que tiene la pagina. 
Las publicaciones creadas.
Los ultimos comentarios.
Solapa de contactos.
Y un panel donde podras dejar un comentario, si es que estas logeado.


- Publicaciones: Se muestran todas las publicaciones y permite acceder a cada una de ellas para verlas en su totalidad.
                 Al ingresar a cada publicacion se puede dejar un "Me Gusta" y un comentario.

- Ingresar - Iniciar : Redirecciona a la vista donde podras logearte.

- Ingresar - Registrarte: Redirecciona a la vista donde podras Registrarte.

- Usuario Logueado: Podremos acceder a nuevas opciones que se listan a continuacion.
    * La primera es "Editar Perfil", donde podras hacer modificaciones a tus datos de registro.
    * La segunda es "Crear Publicacion", donde podras crear una publicacion. 
    * La tercera es "Mis Publicaciones", donde podras ver tus publicaciones, editarlas, borrarlas y eliminarlas.

    - Mis Publicaciones: Esta vista permite listar todas las publicaciones creadas por el usuario logueado.
        -Ver: Permite ver dicha publicacion.
        -Editar: Permite editar dicha publicacion.
        -Eliminar: Permite eliminar dicha publicacion.

- Acerca de: Redirecciona al resumen del proyecto e informacion de los desarrolladores. 


*Pre-requisitos 📋

    Tener las librerias instaladas de requeriments.txt, para ello debemos ejecutar en consola el siguiente comando :
    python -m pip install -r .\requirements.txt
    

*Ejecutando las pruebas ⚙️

    Ingresar a tests.py
    Ejecutar ( python manage.py test ) 


*Construido con 🛠️

    Python - Lenguaje de programacion.
    Django - Framework de desarrollo web de código abierto.


*Autores ✒️

    Matias Alegre 
    Matias Fernandez 
    Matias Miranda

*Version 1.0

*Licencia 📄

*Este proyecto está bajo la Licencia (MillasViajeras 2022) - mira el archivo LICENSE.md para detalles

*Expresiones de Gratitud 🎁

Principalmente a Lucas Trubiano nuestro profesor y a todos los tutores de este curso de Python.

*Comenta a otros sobre este proyecto 📢

