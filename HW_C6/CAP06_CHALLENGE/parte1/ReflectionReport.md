# Reporte de Reflexión

## Cobertura de Pruebas
- **Porcentaje de cobertura alcanzado**: 100%
- Todas las líneas de código relevantes en el archivo `func.py` están cubiertas por las pruebas unitarias.

## Desafíos encontrados
1. **Manejo de entradas no válidas**:
   - Fue un desafío manejar entradas como `True`, `False` y números flotantes que son equivalentes a enteros. Esto requirió una validación cuidadosa para garantizar que la función se comportara correctamente en todos los casos.

2. **Optimización de la función**:
   - Aprendí que verificar divisibilidad solo hasta la raíz cuadrada del número mejora significativamente la eficiencia de la función, especialmente para números grandes.

3. **Escribir pruebas exhaustivas**:
   - Fue un reto identificar todos los casos límite y edge cases, como números negativos, entradas no numéricas y números flotantes con precisión.

## Soluciones implementadas
- Se utilizó `math.isclose` para manejar imprecisiones en números flotantes.
- Se agregó una validación explícita para excluir `True` y `False` como entradas válidas.
- Se escribieron pruebas unitarias utilizando `pytest` para cubrir todos los casos posibles.

## Aprendizajes
- **Importancia del testing**:
  - Escribir pruebas unitarias me ayudó a identificar errores en la lógica de la función y a mejorar su robustez.
  - Las pruebas también sirvieron como documentación viva del comportamiento esperado de la función.

- **Herramientas de testing**:
  - Aprendí a usar `pytest` y `pytest-cov` para escribir pruebas y medir la cobertura de código, lo que garantiza que todas las partes críticas de la función estén probadas.

- **Mejores prácticas**:
  - Validar entradas y manejar excepciones de manera explícita mejora la calidad del código y facilita su mantenimiento.

## Conclusión
El proceso de escribir pruebas unitarias y mejorar la función `es_primo` fue una experiencia valiosa. Me permitió comprender la importancia del testing en el desarrollo de software y cómo puede prevenir errores en etapas tempranas del desarrollo.