# Sistema de Gestión de Reservas de Laboratorios

Proyecto desarrollado con Django para gestionar reservas de laboratorios académicos mediante autenticación, roles y CRUD completo.

---

# Integrantes

* Desarrollador 1
* Desarrollador 2
* Desarrollador 3
* Desarrollador 4
* Desarrollador 5

---

# Tecnologías utilizadas

* Python
* Django 6
* SQLite3
* Bootstrap 5
* HTML5
* CSS3

---

# Funcionalidades

## Autenticación

* Registro de docentes
* Registro de administradores
* Inicio de sesión
* Cierre de sesión

---

## Roles

### Docentes

* Crear reservas
* Editar reservas pendientes
* Eliminar reservas pendientes
* Visualizar reservas

### Administradores

* Aprobar reservas
* Rechazar reservas
* Visualizar reservas
* Exportar reservas CSV

---

# CRUD implementado

| Operación | Funcionalidad    |
| --------- | ---------------- |
| CREATE    | Crear reserva    |
| READ      | Ver reservas     |
| UPDATE    | Editar reserva   |
| DELETE    | Eliminar reserva |

---

# Filtros implementados

* Filtrar por fecha
* Filtrar por laboratorio

---

# Exportación

* Exportar reservas en formato CSV

---

# Estructura del proyecto

GestionLaboratorio/
│
├── GestionLaboratorio/
│   ├── settings.py
│   ├── urls.py
│   └── templates/
│
├── reservas/
│   ├── migrations/
│   ├── templates/
│   │   └── reservas/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md

---

# Instalación del proyecto

## 1. Clonar repositorio

git clone URL_DEL_REPOSITORIO

---

## 2. Entrar al proyecto

cd GestionLaboratorio

---

## 3. Crear entorno virtual

python -m venv venv

---

## 4. Activar entorno virtual

### Windows

venv\Scripts\activate

---

## 5. Instalar Django

pip install django

---

# Migraciones

## Crear migraciones

python manage.py makemigrations

---

## Aplicar migraciones

python manage.py migrate

---

# Crear superusuario

python manage.py createsuperuser

---

# Ejecutar servidor

python manage.py runserver

---

# Acceso al sistema

## Página principal

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Panel administrador

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

# Credenciales de prueba

## Superusuario

Usuario: gadier
Contraseña: 12345678

---

## Administrador

Usuario: admin1
Contraseña: sorry123

---

## Docente

Usuario: docente2
Contraseña: sorry123

---

# Configuración importante

Después de crear el superusuario:

1. Entrar al panel admin
2. Ir a Groups
3. Crear los grupos:

* Docentes
* Administradores

---

# Templates utilizados

## Templates globales

* base.html
* login.html
* registro_docente.html
* registro_administrador.html

---

## Templates CRUD

* lista.html
* form.html
* eliminar.html

---

# Validaciones implementadas

* Validación de horarios
* Evitar conflictos de reservas
* Restricción de edición a reservas pendientes
* Restricción por roles

---

# Seguridad

* LoginRequiredMixin
* UserPassesTestMixin
* CSRF Protection
* Roles con Groups de Django

---

# Comandos Git utilizados

## Crear rama

git checkout -b feature/visualizacion

---

## Guardar cambios

git add .
git commit -m "visualizacion"
git push origin feature/visualizacion

---

# Estado del proyecto

Proyecto funcional con:

* Sistema de autenticación
* CRUD completo
* Roles y permisos
* Filtros
* Exportación CSV
* Diseño responsive
* Interfaz moderna
