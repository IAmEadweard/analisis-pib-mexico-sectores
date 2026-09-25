<div style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px; background-color: #fdfdfd;">

  <h1 style="text-align: center; color: #2c3e50;">
    📊 Análisis del PIB de México por Sector Económico (1994–2026)
  </h1>

  <p style="color: #34495e;">
    Este proyecto consiste en un <strong>análisis exploratorio de datos (EDA)</strong> del Producto Interno Bruto de México desagregado por <strong>20 sectores económicos</strong> (clasificación SCIAN), con series de 1994 a 2026. El objetivo fue identificar los sectores de mayor peso en la economía mexicana y visualizar su evolución a lo largo de 32 años, utilizando <strong>Python</strong> con las librerías <strong>pandas</strong> y <strong>matplotlib</strong>.
  </p>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #2980b9;">🛠️ Herramientas utilizadas</h2>
  <ul style="color: #34495e;">
    <li><strong>Python</strong> – lenguaje principal del análisis</li>
    <li><strong>pandas</strong> – carga, limpieza, transformación y análisis de datos</li>
    <li><strong>matplotlib</strong> – visualización de series temporales</li>
    <li><strong>INEGI</strong> – fuente oficial de los datos</li>
  </ul>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #2980b9;">🔍 Metodología</h2>
  <ol style="color: #34495e;">
    <li><strong>Carga y exploración</strong> del dataset (660 registros, 20 sectores, 33 años).</li>
    <li><strong>Transformación</strong> de los datos de formato largo a formato ancho con <code>pivot</code>, para estructurar las series temporales por sector.</li>
    <li><strong>Identificación</strong> de los 5 sectores con mayor PIB promedio mediante <code>groupby</code> y <code>sort_values</code>.</li>
    <li><strong>Visualización</strong> de las series históricas con gráficos de líneas.</li>
  </ol>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #2980b9;">📈 Resultados</h2>
  <img src="Figure_1.png" alt="Evolución del PIB por sector (1994-2026)" style="max-width: 100%; border: 1px solid #ccc; border-radius: 4px;">

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #16a085;">💡 Principales hallazgos</h2>
  <ul style="color: #34495e;">
    <li><strong>Las industrias manufactureras son el sector dominante</strong> de la economía mexicana: su PIB es más del doble que el del segundo sector (servicios inmobiliarios y de alquiler), con ~1.77 billones en su pico (2025).</li>
    <li>Se observa una <strong>caída visible en 2020 en todos los sectores</strong>, correspondiente al impacto de la pandemia de COVID-19, seguida de una recuperación acelerada en 2021.</li>
    <li>Los sectores de <strong>comercio al por menor, comercio al por mayor y transportes</strong> muestran una trayectoria estable y muy similar entre sí, con leve desaceleración hacia 2026.</li>
    <li>Los <strong>servicios inmobiliarios</strong> crecen de forma sostenida y constante durante todo el periodo, sin contracciones marcadas.</li>
  </ul>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #8e44ad;">📊 Conclusión</h2>
  <p style="color: #34495e;">
    El análisis confirma que la economía mexicana tiene un claro motor en la <strong>industria manufacturera</strong>, cuyo peso se ha mantenido y ampliado durante tres décadas, mientras que los servicios —inmobiliarios, comercio y transportes— forman una base estable y creciente. La crisis de 2020 afectó a todos los sectores por igual, pero la recuperación posterior fue generalizada, lo que refleja la resiliencia estructural de la economía.
  </p>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #c0392b;">⚠️ Limitaciones</h2>
  <p style="color: #34495e;">
    Los valores del dataset corresponden a cifras <strong>nominales</strong> (no ajustadas por inflación), por lo que el crecimiento mostrado refleja tanto el crecimiento real del sector como el efecto de los precios.
  </p>
  <p style="background-color: #f5f5dc; padding: 10px; border-radius: 4px; color: #7f8c8d;">
    <strong>Trabajo futuro:</strong> complementar con series a precios constantes, realizar pronósticos con modelos de series temporales (ARIMA / Prophet) y analizar la participación porcentual y las tasas de crecimiento anual compuesto (CAGR) por sector.
  </p>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #2980b9;">🚀 Cómo ejecutar el proyecto</h2>
  <ol style="color: #34495e;">
    <li>Clona el repositorio:</li>
  </ol>
  <pre style="background-color: #2c3e50; color: #ecf0f1; padding: 10px; border-radius: 4px;">git clone https://github.com/tu-usuario/analisis-pib-mexico-sectores.git</pre>
  <ol start="2" style="color: #34495e;">
    <li>Instala las dependencias:</li>
  </ol>
  <pre style="background-color: #2c3e50; color: #ecf0f1; padding: 10px; border-radius: 4px;">pip install pandas matplotlib</pre>
  <ol start="3" style="color: #34495e;">
    <li>Ejecuta el script:</li>
  </ol>
  <pre style="background-color: #2c3e50; color: #ecf0f1; padding: 10px; border-radius: 4px;">python analisis.py</pre>

  <hr style="border-top: 1px solid #ccc;">

  <h2 style="color: #16a085;">👤 Autor</h2>
  <p style="color: #34495e;">
    [Eduardo Fabian Vidaca Araujo] – <a href="https://www.linkedin.com/in/eduardo-fabian-vidaca-araujo-it-engineer//" style="color: #2980b9;">LinkedIn</a> – eduardovidaca2022@gmail.com
  </p>

</div>
