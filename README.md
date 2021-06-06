# sogooddata-madrid-salud-polucion

## Descripción.
Impacto de la **calidad del aire** en la **salud respitaria** en la ciudad de **Madrid**: predicción del número de ingresos hospitalarios por enfermedades respiratorias en función de los niveles de contaminación.

## Estructura del proyecto.
 
    ├── data
    │   ├── external            # Datos inmutables, extraídos de terceros.
    │   │   ├── calidad_aire
    │   │   ├── hospitalizaciones
    │   │   ├── polen
    │   │   └── tabaquismo
    │   ├── interim             # Inputs de src/features, generados por scripts de src/data a partir de data/external.
    │   ├── processed           # Inputs de los src/model, generados por scripts de src/features.
    │   └── raw                 # Copia local de subsets de data/external, para poder trabajar en caso de problemas en la red.
    ├── docs                    # Documentación, FAQs, casos de uso.
    ├── models                  # Scripts de los distintos modelos entrenados.
    ├── notebooks               # Análisis ad-hoc y POCs.
    ├── src
    │   ├── data                # Scripts de ingesta de fuentes de datos de terceros y transformación al estado previo a feature engineering.
    │   ├── features            # Scripts de feature engineering para generar los inputs de los modelos.
    │   └── model               # Scripts de definición y entrenamiento de modelos.
    ├── gitignore
    ├── LICENSE
    └── README.md

## Setup

1. Clonar repositorio en local.
2. Ejecutar ./generar_estructura_directorios.ipynb.
3. Copiar credentials.py en ./notebooks.
4. Copiar CMBD_6_20181217-135856.xlsx en ./data/external/hospitalizaciones.
5. Copiar los ficheros datos??.csv, datos??????.csv y magnitudes_unidades_tecnicas_medida.csv en ./data/external/calidad_aire.
6. Copiar inclasns_tabaquismo.csv en ./data/external/tabaquismo.
7. Copiar calendario_polinico_espana.csv en ./data/external/polen.
8. Ejecutar ./notebooks/poc.ipynb.

## Fuentes de datos
### Hospitalizaciones (ICMBD)
* Extracción de datos de http://icmbd.es/login-success.do, con información de cada hospitalización por enfermedad respiratoria de 2008 a 2015 en la comunidad de Madrid.
* Solo podemos trabajar con esta extracción porque no tenemos usuario para acceder al sistema; sería muy útil disponer de uno para poder acceder a una ventana temporal más amplia, al diccionario de datos, o a más variables.
### Calidad del aire
* Datos públicos en formato csv con información diaria de las estaciones de medición https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default
* Como primera aproximación se ha cargado la media de cada compuesto; la serie histórica generada muestra picos puntuales para algunos compuestos que, a falta de más análisis, parecen errores de medida. Sería necesario realizar EDA, DQ y definir una metodología mejor para integrar estos datos en el proyecto.
* Como segunda aproximación, buscar serie histórica de indicadores de calidad del aire (ICA) o en su defecto construirlo, a partir de las medidas de las estaciones de medición, con la metodologia indicada en http://www.mambiente.munimadrid.es/opencms/opencms/calaire/SistemaIntegral/SistInformacion.html
### Tabaquismo (INCLASNS)
* Datos públicos de indicadores del sistema nacional de salud, permite varios tipos de agregación, filtrado de datos y exportación a EXCEL http://inclasns.msssi.es/?show=true
* Como primera aproximación, se han cargado porcentajes de incidencia en la población  nivel [AÑO, SEXO, CCAA/NACIONAL]. Las encuestas no son anuales así que será necesario interpolar para dar valores a nivel [FECHA, SEXO].
* La Encuesta Nacional de Salud de España https://www.mscbs.gob.es/estadEstudios/estadisticas/encuestaNacional/encuestaNac2017/encuestaResDetall2017.htm (ENSE YYYY) ofrece datos desagregados por rango de edad, se publican en PDF pero su carga requiere una ETL más complicada.
### Polen
* Como primera aproximación se ha imputado manualmente un calendario polínico de España, y como segunda opción, más laboriosa, contemplaría imputar a mano la tabla de la página 30 del siguiente documento http://www.madrid.org/bvirtual/BVCM009130.pdf. Idealmente debería cargarse la información histórica de las estaciones de seguiemiento, pero no se ha encontrado un repositorio con suficiente histórico.
### Climatología
* Llamada por programa a la API del proyecto Open Data de AEMET https://opendata.aemet.es/centrodedescargas/inicio para descargar datos meteorológicos a nivel diario de la estación de Retiro. La contraseña caduca cada 5 días, debe solicitarse una nueva en https://opendata.aemet.es/centrodedescargas/altaUsuario? se envía de forma inmediata al correo electrónico.
### Demografía
* De cara a la definición del target en los modelos de predicción de ingresos hospitalarios, si se optar por predecir la incidencia por 100,000 habitantes será necesario disponer de datos demográficos para poder construir la variable. Todavía no se ha abordado la generación de este dataset.
