test_sequra project

Entorno utilizado:

python version 3.7.2
Django=3.2


Solution
He implementado las clases segun la propuesta. Para guardar los calculos de las comisones a los vendedores hecerado una tabla con el identificados de venderor, la semana y la cantidad total de la semana.
El calculo se deberia hacer en una tarea de background, pero por tiempo, he realizado el calculo a partir de un un get que recibe la semana en la que se quiere realizar. Realiza los calculos y los guarda en la tabla Disbursements. Por simplicidad se guarda el numero de la semana y no se ha tenido en cuenta los años. Simplemente es para trabajar con los datos proporcionados.
Para el caso de la consulta de las comisiones para una semana dada se pasan los parametros por el get (week=&merchant=)


Testing

Test para comprobar que se introducen los datos del calculo de las comisiones para una semana data por vendedor:
http://127.0.0.1:8000/data/?week=5
Si todo funciona correctamente devuelve los siguiente:
Creados datos para la semana 5 
Y a traves del admin de django se puede comprobar que se han creado los registros en la tabla Disbursements.

Test para comprobar que funcionan las consultas:

http://127.0.0.1:8000/disbur/?week=5

Se pide la relación de todos los vendedores con las comisones asociadas a la semana 5. Si todo esta correcto se devuelve un págian con esa información:

Flatley-Rowe - 5 - 42.49
Streich, Klocko and Marvin - 5 - 34.75
Towne-Waelchi - 5 - 41.75
Lubowitz, Hessel and Berge - 5 - 51.52
Streich-Koepp - 5 - 34.21
Pfeffer, Wiza and Jacobson - 5 - 30.96
Mayer, Kemmer and Schumm - 5 - 32.59
Zulauf-Roberts - 5 - 18.81
Dietrich-Ortiz - 5 - 47.12
Weissnat, Hackett and Purdy - 5 - 38.20
Von and Sons - 5 - 39.46
Oga Inc - 5 - 31.81
Schoen Inc - 5 - 31.43
Hodkiewicz-Stehr - 5 - 39.35 

Y por último para la consulta de las comisiones de un vendedor en particular en una semana es:
http://127.0.0.1:8000/disbur/?week=5&merchant=5
Obteniendo una página con el resuldo
Von and Sons - 5 - 39.46 


La carga de los datos se realizó a traves de la interfaz admin de django. Hubo que quietar la definición de record para que cargasen correctamente.


Otras versiones de librerias utilizadas

ip freeze
asgiref==3.5.2
defusedxml==0.7.1
diff-match-patch==20200713
Django==3.2
django-import-export==2.8.0
et-xmlfile==1.1.0
MarkupPy==1.14
odfpy==1.4.1
openpyxl==3.0.10
pytz==2022.1
PyYAML==6.0
sqlparse==0.4.2
tablib==3.2.1
typing-extensions==4.2.0
xlrd==2.0.1
xlwt==1.3.0
