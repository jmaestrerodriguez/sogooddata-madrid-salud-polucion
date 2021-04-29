# sogooddata-madrid-salud-polucion

## Descripción.
Impacto de la **calidad del aire** en la **salud respitaria** en la ciudad de **Madrid**: predicción del número de ingresos hospitalarios por enfermedades respiratorias en función de los niveles de contaminación.

## Estructura del proyecto.
 
    ├── data
    │   ├── external            # Datos inmutables, extraídos de terceros.
    │   ├── interim             # Inputs de src/features, generados por scripts de src/data a partir de data/external.
    │   ├── processed           # Inputs de los src/model, generados por scripts de src/features.
    │   └── raw                 # Copia local de subsets de data/external, para poder trabajar en caso de problemas en la red.
    ├── docs                    # Documentación, FAQs, casos de uso.
    ├── models                  # Ficheros de los distintos modelos entrenados
    ├── notebooks               # Análisis ad-hoc y POCs.
    ├── src
    │   ├── data                # Scripts de ingesta de fuentes de datos de terceros y transformación al estado previo a feature engineering.
    │   ├── features            # Scripts de feature engineering para generar los inputs de los modelos.
    │   └── model               # Scripts de definición y entrenamiento de modelos.
    ├── gitignore
    ├── LICENSE
    └── README.md
