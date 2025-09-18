# Proyecto: Regularización L1, L2 y Elastic Net

Este proyecto contiene un notebook de Jupyter que demuestra el uso y los efectos de las técnicas de regularización L1 (Lasso), L2 (Ridge) y Elastic Net en modelos de regresión lineal.

## Pasos para la Ejecución

A continuación se describen dos métodos para configurar y ejecutar el entorno de desarrollo necesario para este proyecto.

### Opción 1: Usando un Entorno Virtual de Python

Este es el método tradicional si no utilizas Docker.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/osrodgon/P5_G1_Task.git
    cd P5_G1_Task
    ```

2.  **Crear y activar un entorno virtual:**
    *   En macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   En Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instalar las dependencias:**
    El archivo `requirements.txt` contiene todas las librerías necesarias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar Jupyter:**
    Una vez instaladas las dependencias, puedes iniciar Jupyter Lab o Jupyter Notebook para abrir y ejecutar el notebook del proyecto.
    ```bash
    jupyter lab
    ```
    o
    ```bash
    jupyter notebook
    ```

### Opción 2: Usando Dev Containers (con VS Code)

Este método es el recomendado si tienes Docker instalado, ya que automatiza toda la configuración del entorno. La configuración está definida en el archivo `.devcontainer/devcontainer.json`.

1.  **Requisitos previos:**
    *   Docker Desktop
    *   Visual Studio Code
    *   La extensión Dev Containers para VS Code.

2.  **Abrir en el contenedor de desarrollo:**
    *   Clona el repositorio y ábrelo con VS Code.
    *   VS Code detectará automáticamente el archivo `.devcontainer/devcontainer.json` y te mostrará una notificación preguntando si deseas reabrir el proyecto en un contenedor. Haz clic en **"Reopen in Container"**.
    *   El contenedor se construirá automáticamente, instalará Python y todas las dependencias listadas en `requirements.txt` usando el comando `postCreateCommand`.
    *   Una vez que el contenedor esté listo, puedes abrir el notebook (`.ipynb`) y ejecutarlo directamente dentro de VS Code, aprovechando un entorno aislado y reproducible.
