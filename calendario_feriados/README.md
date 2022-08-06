## calendario_feriados

Implementación simple para obtener el calendario de días feriados desde en API de Google Calendar.

## Configuración

Es necesario configurar python para conectarse con el API de Google

https://developers.google.com/docs/api/quickstart/python
 
Se deben guardar los archivos con las credenciales necesarias:

- credentials.json - archivo proporcionado por Google para validar las credenciales por primera vez
- token.json - archivo generado cuando se ejecute por primera vez el script

## Scripts

### holidays.py

Se conecta al API de Google Calendar y descarga el calendario de días feriados de Panamá al archivo **holidays.json**

### extract.py

Extrae las fechas feriadas del archivo **holidays.json** y las guarda en el archivo **dates.txt** para posterior uso