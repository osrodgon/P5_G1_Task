# Proyecto: Regularización L1, L2 y Elastic Net

Este proyecto contiene un notebook de Jupyter que demuestra el uso y los efectos de las técnicas de regularización L1 (Lasso), L2 (Ridge) y Elastic Net en modelos de regresión lineal.

## Pasos para la Ejecución

A continuación se describen dos métodos para configurar y ejecutar el entorno de desarrollo necesario para este proyecto.

### Opción 1: Usando un Entorno Virtual de Python

Este es el método tradicional si no utilizas Docker.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/L1-L2-Elastic-Net.git
    cd L1-L2-Elastic-Net
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

## Contenido del Notebook

El notebook del proyecto (por ejemplo, `elastic_net.ipynb`) está estructurado para guiar al usuario a través de los conceptos y la aplicación de la regularización en modelos de regresión.

1.  **Introducción a la Regularización:**
    *   Se explica el problema del sobreajuste (overfitting) en modelos de machine learning.
    *   Se introduce la regularización como una técnica para penalizar la complejidad del modelo y mejorar su capacidad de generalización en datos no vistos.

2.  **Generación de Datos:**
    *   Se crea un conjunto de datos sintético para un problema de regresión. Este conjunto de datos está diseñado para tener características (features) que son irrelevantes o redundantes, un escenario donde la regularización es particularmente útil.

3.  **Regularización L1 (Lasso):**
    *   Se explica teóricamente cómo la regularización Lasso añade una penalización igual al valor absoluto de la magnitud de los coeficientes (`alpha * sum(|w|)`) a la función de coste.
    *   Se implementa un modelo de Regresión Lasso usando Scikit-learn.
    *   Se analizan los coeficientes del modelo, observando cómo Lasso tiende a reducir a cero los coeficientes de las características menos importantes, realizando así una selección de características automática.

4.  **Regularización L2 (Ridge):**
    *   Se explica cómo la regularización Ridge añade una penalización igual al cuadrado de la magnitud de los coeficientes (`alpha * sum(w^2)`) a la función de coste.
    *   Se implementa un modelo de Regresión Ridge.
    *   Se comparan los coeficientes con los de un modelo de regresión lineal simple y con los de Lasso, notando que Ridge reduce los coeficientes pero no los lleva exactamente a cero.

5.  **Regularización Elastic Net:**
    *   Se presenta Elastic Net como una combinación de las penalizaciones L1 y L2. La función de coste incluye ambos términos, ponderados por un hiperparámetro `l1_ratio`.
    *   Se discuten sus ventajas, como su capacidad para manejar características correlacionadas (agrupando y seleccionando variables juntas) y ser un término medio entre Lasso y Ridge.
    *   Se implementa un modelo Elastic Net y se ajustan sus hiperparámetros (`alpha` y `l1_ratio`).

6.  **Comparación y Conclusiones:**
    *   Se comparan el rendimiento (usando métricas como el Error Cuadrático Medio) y los coeficientes de los tres modelos regularizados frente al modelo de regresión lineal simple.
    *   Se utilizan visualizaciones para mostrar el efecto de cada tipo de regularización en los coeficientes del modelo a medida que varía el hiperparámetro de regularización `alpha`.
    *   Se extraen conclusiones sobre cuándo es apropiado usar cada técnica de regularización en función de las características del problema y los datos.
