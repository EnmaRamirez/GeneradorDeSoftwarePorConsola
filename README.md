# GenSoft DSL - Generador de Proyectos de Software por Consola

## Descripción General

**GenSoft DSL** es un compilador/generador de código desarrollado para el curso de Compiladores.
El proyecto implementa un **Lenguaje Específico de Dominio (DSL)** capaz de definir proyectos de software de manera declarativa mediante archivos `.gensoft` o `.scf`.

El compilador procesa el archivo fuente y genera automáticamente una estructura funcional de proyecto utilizando tecnologías modernas como:

* FastAPI
* Docker
* Swagger/OpenAPI
* Python
* ANTLR4

El sistema implementa todas las fases clásicas de compilación:

* Análisis Léxico
* Análisis Sintáctico
* Análisis Semántico
* Optimización Intermedia
* Generación de Código

---

# Objetivos del Proyecto

El objetivo principal es construir un compilador completo para un DSL propio que permita:

* Definir proyectos mediante sintaxis declarativa.
* Validar sintaxis y semántica del lenguaje.
* Aplicar optimizaciones intermedias.
* Generar automáticamente proyectos funcionales.
* Exponer una interfaz CLI profesional e instalable globalmente.

---

# Tecnologías Utilizadas

* Python 3.11+
* ANTLR4
* FastAPI
* Docker
* Typer (CLI)
* Pydantic
* Uvicorn

---

# Arquitectura del Compilador

```text
Archivo .gensoft
        ↓
ANTLR Lexer
        ↓
ANTLR Parser
        ↓
Árbol Sintáctico (AST)
        ↓
Análisis Semántico
        ↓
Optimizador
        ↓
Generador de Código
        ↓
Proyecto FastAPI + Docker
```

---

# Instalación

## 1. Crear entorno virtual

```bash
python -m venv .venv
```

## 2. Activar entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Instalar la herramienta globalmente

```bash
pip install -e .
```

Después de esto, el comando `proyectocli` quedará disponible desde la terminal.

---

# Uso de la CLI

## Crear plantilla base

```bash
proyectocli init
```

Genera automáticamente un archivo base:

```text
proyecto.gensoft
```

---

## Validar archivo DSL

```bash
proyectocli check proyecto.gensoft
```

Realiza:

* análisis léxico
* análisis sintáctico
* análisis semántico

Sin generar archivos.

---

## Generar proyecto

```bash
proyectocli build proyecto.gensoft
```

Genera automáticamente:

* estructura de carpetas
* archivos base
* rutas FastAPI
* modelos
* Dockerfile
* README
* configuración inicial

---

## Generar en directorio específico

```bash
proyectocli build proyecto.gensoft --output ./salida
```

---

## Vista previa sin generar archivos

```bash
proyectocli build proyecto.gensoft --preview
```

---

## Activar optimizaciones

```bash
proyectocli build proyecto.gensoft --optimize-level 1
```

---

## Listar templates disponibles

```bash
proyectocli templates --list
```

Templates soportados:

* web
* api
* consola

---

# Ejecutar el proyecto generado

Después de generar un proyecto con `proyectocli build`, entra en la carpeta de salida donde se creó el proyecto. Por ejemplo:

```bash
cd salida/MiProyecto
```

### Ejecutar localmente con Uvicorn

Activa el entorno virtual y ejecuta la aplicación:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

> `0.0.0.0` indica que el servidor escucha en todas las interfaces, pero en el navegador debes usar `http://localhost:8000` o `http://127.0.0.1:8000`.

### Ejecutar con Docker

```bash
docker build -t miproyecto .
docker run -p 8000:8000 miproyecto
```

En el navegador usa:

```text
http://localhost:8000
```

### Nota importante

* `http://0.0.0.0:8000` no debe usarse en el navegador.
* Si accedes desde otra máquina, usa la IP de tu equipo en la red local, por ejemplo `http://192.168.x.x:8000`.
* Si Uvicorn muestra `Running on http://0.0.0.0:8000`, la aplicación está funcionando correctamente.

---

# Sintaxis del DSL

El lenguaje permite declarar proyectos, módulos y campos de manera declarativa.

---

# Ejemplo de Archivo `.gensoft`

```gensoft
proyecto MiProyecto tipo web {

    modulo usuarios {

        campo id: entero;
        campo nombre: string;
        campo activo: booleano;
    }

    modulo productos {

        campo id: entero;
        campo titulo: string;
        campo precio: decimal;
    }
}

generar MiProyecto;
```

---

# Gramática ANTLR

El compilador utiliza ANTLR4 para generar automáticamente el Lexer y Parser.

Archivo principal:

```text
grammar/GenSoft.g4
```

---

# Gramática EBNF

```ebnf
programa ::= { declaracionProyecto | comandoGenerar } EOF

declaracionProyecto ::=
    "proyecto" ID "tipo" ("web" | "consola" | "api") "{" { modulo } "}"

modulo ::= "modulo" ID "{" { campo } "}"

campo ::= "campo" ID ":" ("string" | "entero" | "decimal" | "booleano") ";"

comandoGenerar ::= "generar" ID ";"
```

---

# Generación del Lexer y Parser con ANTLR

## Requisitos

* Java instalado
* antlr4.jar disponible

## Generar archivos ANTLR

```bash
cd grammar

java -jar ..\tools\antlr4.jar -Dlanguage=Python3 GenSoft.g4 -o generated
```

Esto genera automáticamente:

* GenSoftLexer.py
* GenSoftParser.py
* GenSoftVisitor.py
* GenSoftListener.py

---

# Fases del Compilador

## 1. Análisis Léxico

Responsable de tokenizar el archivo fuente `.gensoft`.

Archivo principal:

```text
lexer/lexer_wrapper.py
```

Funciones:

* reconocimiento de tokens
* validación de símbolos
* manejo de errores léxicos

---

## 2. Análisis Sintáctico

Construye el árbol sintáctico usando ANTLR4.

Archivo principal:

```text
grammar/GenSoft.g4
```

Funciones:

* validación de estructura gramatical
* construcción del AST

---

## 3. Análisis Semántico

Verifica reglas semánticas del lenguaje.

Archivo principal:

```text
semantic/analyzer.py
```

Validaciones:

* tipos válidos
* proyectos existentes
* módulos correctos
* generación válida

---

## 4. Optimización Intermedia

Archivo principal:

```text
optimizer/optimizer.py
```

Optimizaciones implementadas:

### 1. Normalización de texto

Convierte valores a minúsculas.

Ejemplo:

```text
FastAPI → fastapi
```

---

### 2. Eliminación de dependencias duplicadas

Ejemplo:

```text
[fastapi, fastapi, uvicorn]
↓
[fastapi, uvicorn]
```

---

### 3. Asignación de valores por defecto

Campos agregados automáticamente:

* version
* author
* description
* output

---

## 5. Generación de Código

Archivo principal:

```text
compiler/generator/project_generator.py
```

Genera automáticamente:

* FastAPI app
* rutas CRUD
* modelos
* Dockerfile
* README
* templates HTML
* estructura de carpetas

---

# Docker

El proyecto generado incluye soporte Docker automático.

## Construir imagen

```bash
docker build -t miproyecto .
```

## Ejecutar contenedor

```bash
docker run -p 8000:8000 miproyecto
```

---

# Swagger / FastAPI

Los proyectos generados incluyen documentación automática mediante Swagger.

Disponible en:

```text
http://localhost:8000/docs
```

---

# Estructura del Proyecto

```text
ProyectoCompiladores/
│
├── cli.py
├── pyproject.toml
├── requirements.txt
├── README.md
│
├── compiler/
│   ├── generator/
│   │   └── project_generator.py
│   └── scf_ast.py
│
├── lexer/
│   └── lexer_wrapper.py
│
├── semantic/
│   └── analyzer.py
│
├── optimizer/
│   ├── optimizer.py
│   └── rules.py
│
├── grammar/
│   ├── GenSoft.g4
│   └── generated/
│
├── examples/
│
├── docs/
│
└── tools/
    └── antlr4.jar
```

---

# Ejemplos Incluidos

## Archivo válido

```text
examples/ejemplo1.gensoft
```

## Archivo con errores

```text
examples/ejemplo_con_errores.gensoft
```

---

# Manejo de Errores

El compilador muestra errores descriptivos indicando:

* línea
* columna
* tipo de error
* símbolo esperado

Ejemplo:

```text
[parser] Línea 4:20 → símbolo inesperado 'int'
```

---

# Características Implementadas

* DSL propio
* Lexer con ANTLR
* Parser con ANTLR
* AST
* Semántica
* Optimizaciones
* CLI profesional
* Generación automática
* FastAPI
* Docker
* Swagger/OpenAPI
* Instalación global
* Templates
* Preview de generación
* Manejo de errores

---

# Estado del Proyecto

Proyecto funcional y completamente operativo.

Todas las fases principales del compilador fueron implementadas correctamente y el sistema genera proyectos reales funcionales automáticamente.

---

# Integrantes de Grupo
Enma Leticia Ramírez Castro 0907-23-18206
Fredy Aníbal Cardona Montenegro 0907-23-22830
Luis Gustavo Ramírez Berganza 0907-23-8082
Edgar Leonel Barco Cruz 0907-19-12485

Proyecto desarrollado para el curso de Compiladores

