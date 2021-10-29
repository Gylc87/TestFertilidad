#Gildardo Yair Loera Contreras - 19110230
#Practica 2 - Motor de Inferencia y Motor de Explicacion.

import tkinter as tk
from tkinter import messagebox
import os
import array

class FormularioFertilidad(tk.Tk):
    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    def inicializar_gui(self):
        self.title('Test de Fertilidad')
        self.minsize(750, 450)
def main():
    app = FormularioFertilidad()
    app.mainloop()

if __name__ == '__main__':
    main()

#PreguntasMujer 11
arrayPreguntasMujer = ['¿Qué edad tienes?','¿Fumas?','¿Tienes sobrepeso o bajo peso?','¿Qué tan regulares son tus periodos menstruales?','¿Presentas sangrado o manchado entre tus periodos?','¿Tienes historial de enfermedades de transmisión sexual (ETS)?','¿Tienes dolor durante tu menstruación o durante las relaciones sexuales?',
'¿Bebes alcohol en exceso o haces uso recreativo de drogas?','¿Tienes historial de abortos recurrentes?','¿Sufres de algún problema médico crónico?','¿Has estado expuesta a radiación o medicamentos quimioterapéuticos?']
#PreguntasHombre 9
arrayPreguntasHombre = ['¿Qué edad tienes?','¿Fumas?','¿Tienes sobrepeso o bajo peso?','¿Tienes historial de enfermedades de transmisión sexual (ETS)?','¿Bebes alcohol en exceso o haces uso recreativo de drogas?',
'¿Sufres de algún problema médico crónico?','¿Has estado expuesto a radiación o medicamentos quimioterapéuticos?',
'¿Te expones frecuentemente a ambientes con temperatura elevada y mala ventilación como saunas, vapores u hornos?',
'¿Presentas dolor o mayor sensibilidad en la region testicular o tienes diagnóstico de varicocele?']


genero = ''
respuesta = ''
total = 0
print("\n\n¿Quieres saber que tan fertil eres?\n\n")
print("La infertilidad no presenta síntomas, y tanto hombres como mujeres pueden padecerla. Un tercio de los casos de infertilidad es causado por factores masculinos, en tanto que un tercio puede atribuirse a factores femeninos y el resto se debe a una combinación de problemas en ambos miembros de la pareja o surge de causas inexplicables\n\n")
os.system("pause")
print("Para iniciar por favor elige tu sexo:")
genero = int(input(
"1 - Mujer\n"
"2 - Hombre\n\n"
))

if genero == 1:
    print("\n Pregunta 1:\n",arrayPreguntasMujer[0],"\n")
    print("Conforme la edad de la mujer avanza, los óvulos tienen menos posibilidades de formar un embrión que se pueda implantar y formar un hijo con un conjunto normal de cromosomas. El proceso de envejecimiento también disminuye la cantidad de óvulos que tiene. Después de la edad de 35 años, su potencial de fertilidad comienza a disminuir. Después de los 40 años, las posibilidades de embarazarse disminuyen rápidamente. Por lo que es importante realizar un diagnóstico certero, ya que la edad es un factor clave para la fertilidad\n")
    respuesta = int(input(
        "1 - Menos de 35 años\n"
        "2 - 35 - 38 años\n"
        "3 - 38+ años\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 2:\n",arrayPreguntasMujer[1],"\n")
    print("Fumar podría tener efectos adversos importantes tanto sobre la calidad de sus óvulos como en la calidad del esperma de tu pareja, por lo tanto puede afectar tu capacidad para embarazarte y de tener un bebé sano. Si fumas, tu fertilidad natural puede disminuir. También puede disminuir prematuramente tu reserva ovárica, envejeciendo sus ovarios a una velocidad mayor a la normal y podría llegar hasta causar menopausia prematura. Si logras embarazarte, los estudios muestran que las fumadoras podrían presentar tienen un mayor riesgo de aborto y menor probabilidad de lograr un nacimiento sano.\n")
    respuesta = int(input(
        "1 - Nunca he fumado\n"
        "2 - Fumaba antes\n"
        "3 - Fumo Actualmente\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 3:\n",arrayPreguntasMujer[2],"\n")
    print("El sobrepeso puede tener efectos sobre la ovulación. Apenas hace poco tiempo se determinó plenamente que el peso también puede afectar, disminuyendo las posibilidades de embarazo. El efecto más importante ocurre cuando el índice de masa corporal (IMC) es de más de 35. Si tienes bajo peso y tu grasa corporal es de 10 a 15 por ciento inferior a la normal, puedes tener problemas para embarazarte. Las mujeres con bajo peso pueden ser incapaces de producir las hormonas necesarias para causar la ovulación, la cual es esencial para la concepción. Para calcular tu índice de masa corporal es necesario realizar una sencilla operación: Se divide la masa en kilogramos (el peso) entre el cuadrado de la estatura expresada en metros (altura).\n")
    respuesta = int(input(
        "1 - IMC 18.5 - 24.9\n"
        "2 - IMC 25.0 - 29.9\n"
        "3 - IMC > 30.0\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 4:\n",arrayPreguntasMujer[3],"\n")
    print("Ya que la ovulación es esencial para tener un bebé, el hecho de tener periodos menstruales irregulares o ausencia de menstruación es riesgo de infertilidad. Si no menstrúas, o si tus ciclos son de más de 35 días o de menos de 25 días, podrías tener un problema de ovulación, una de las principales causas de infertilidad.\n")
    respuesta = int(input(
        "1 - Periodos Regulares\n"
        "2 - Irregulares, pero aproximandamente una vez al mes\n"
        "3 - Muy irregulares o ausentes\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 5:\n",arrayPreguntasMujer[4],"\n")
    print("El sangrado anormal o manchado entre los periodos podría ser una señal de problemas hormonales, fibromas, pólipos, o problemas del útero o cervicales.\n")
    respuesta = int(input(
        "1 - Nunca\n"
        "2 - Rara vez\n"
        "3 - Frecuentemente\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 6:\n",arrayPreguntasMujer[5],"\n")
    print("Las enfermedades de transmisión sexual (ETS) se han añadido a esta lista como uno de los principales causantes de infertilidad tanto en mujeres como en hombres. Si permanecen sin tratamiento, las enfermedades como la gonorrea o clamidia pueden conducir a enfermedad pélvica inflamatoria (EIP). La EIP puede resultar en complicaciones como cicatrices, abortos, embarazo ectópico, y bloqueo de las trompas de Falopio. Todas estas complicaciones pueden afectar tu probabilidad de lograr un embarazo sano.\n")
    respuesta = int(input(
        "1 - Nunca ha tenido una ETS\n"
        "2 - Una ETS sin llegar a una Enfermedad pélvica inflamatoria EPI\n"
        "3 - Enfermedad Pélvica Inflamatoria EPI\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 7:\n",arrayPreguntasMujer[6],"\n")
    print("La endometriosis, la enfermedad tubárica, enfermedad inflamatoria pélvica y los fibromas pueden afectar la fertilidad negativamente y pueden ocasionar dolor durante las relaciones sexuales. Si experimentas dolor pélvico, dolor durante el sexo o dolor anormal durante la menstruación uno de los anteriores puede ser causa de infertilidad.\n")
    respuesta = int(input(
        "1 - Ningun dolor\n"
        "2 - Dolor Leve\n"
        "3 - Dolor Moderado a Severo\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 8:\n",arrayPreguntasMujer[7],"\n")
    print("Se ha demostrado que beber en exceso o usar drogas incrementa las probabilidades de sufrir trastorno ovulatorio o endometriosis. Ambas condiciones pueden dificultar embarazarse y/o de que el embarazo llegue a término. También puede afectar la calidad de los espermatozoides de su pareja.\n")
    respuesta = int(input(
        "1 - No bebo alcohol ni uso drogras\n"
        "2 - Alcohol moderado o cualquier uso de drogas ocasional\n"
        "3 - Consumo intenso de alcohol o uso regular de drogas\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 9:\n",arrayPreguntasMujer[8],"\n")
    print("Los abortos recurrentes pueden ser causados por una anormalidad cromosómica en uno de los padres, problemas con la calidad de los óvulos, anormalidades estructurales del útero o anormalidades hormonales.\n")
    respuesta = int(input(
        "1 - Ninguno o un aborto\n"
        "2 - 2 abortos\n"
        "3 - 3 o mas abortos\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 10:\n",arrayPreguntasMujer[9],"\n")
    print("Los problemas médicos severos como la diabetes, asma, alta presión arterial, artritis reumatoide pueden dificultar el embarazarse. Los medicamentos que se utilizan para tratar estas enfermedades pueden inhibir tu capacidad de concebir o ser dañinas para el bebé no nato.\n")
    respuesta = int(input(
        "1 - Ningún problema médico\n"
        "2 - Problema médico leve\n"
        "3 - Problema médico severo\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 11:\n",arrayPreguntasMujer[10],"\n")
    print("Las mujeres que reciben dosis relativamente altas de quimioterapia o radiación pueden ser más propensas a perder la fertilidad después del tratamiento que las mujeres tratadas con dosis más bajas.\n")
    respuesta = int(input(
        "1 - No\n"
        "2 - Ocasionalmente\n"
        "3 - Frecuente o en tratamientos de quimio o radioterapia\n"
    ))
    total = total + respuesta
    os.system("pause")

    #RESULTADOS MUJER
    print("RESULTADOS\n"
         "TU PUNTUACION ES DE :",total,"\n")
    
    if total <=13 :
        print("La recomendación general es intentar concebir durante un año utilizando algún apoyo para predecir la ovulación para ayudarte a la programación correcta del coito antes de buscar ayuda médica.\n Algunos tipos de apoyo para predecir la ovulación: Tiras de LH (hormona leutenizante), Chequeo frecuente de tu temperatura corporal, cualquier app que indique tus días fértiles")
    elif total > 13 and total <=16:
        print("La recomendación general es intentar concebir durante seis meses antes de buscar ayuda médica a menos que tenga periodos menstruales irregulares, un problema de fertilidad conocido, o más de 35 años; en cuyo caso puede ser buena idea consultar a un especialista en fertilidad para obtener asesoría y una evaluación. Si alguno de sus puntos se deben a problemas por su estilo de vida, debe modificarlo de inmediato. Un buen recurso para obtener información acerca del estilo de vida es Fertility & Lifestyle (Fertilidad y Estilo de Vida). Idealmente los problemas de estilo de vida deben alterarse al comenzar a buscar la concepción, pero todos estos factores se vuelven progresivamente más importantes al involucrarse más en los tratamientos de fertilidad.")
    elif total >=17:
        print("Tienes problemas de fertilidad o ginecológicos conocidos, tienes más de 40 años, no tienes periodos menstruales o elegiste la tercera opción en cualquier factor que no sea un factor de estilo de vida que pueda modificar, te recomendamos ver a un especialista en fertilidad a la brevedad si estás buscando tener un bebé.")
   # print("Resultado: ",total)
elif genero == 2:
    print("\n Pregunta 1:\n",arrayPreguntasHombre[0],"\n")
    print("En el caso masculino, la edad del hombre no es tan influyente en la fertilidad como en el caso de la mujer, ya que la edad fértil del hombre dura mientras el líquido seminal contenga espermatozoides. De media, este periodo empieza a la temprana edad de 14 años y termina a los 60 años.\n")
    respuesta = int(input(
        "1 - Menos de 25 años\n"
        "2 - 25 - 38 años\n"
        "3 - 38+ años\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 2:\n",arrayPreguntasHombre[1],"\n")
    print("En lo que respecta a la fertilidad, el tabaco daña la calidad del esperma de los hombres, además de que la nicotina y algunos tóxicos más que se encuentran en los cigarrillos llevan a que el ADN del espermatozoide se fragmente, lesionándose el material genético del esperma, lo cual lleva a que la fecundación sea muy complicada.\n")
    respuesta = int(input(
        "1 - Nunca he fumado\n"
        "2 - De 1 a 5 cigarrilos al día\n"
        "3 - Mas de 5 cigarrillos al día\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 3:\n",arrayPreguntasHombre[2],"\n")
    print("Los hombres con sobrepeso tienen una peor calidad del esperma que los hombres de peso saludable. El sobrepeso o la obesidad también pueden causar cambios hormonales que reducen la fertilidad y hacen que los hombres estén menos interesado en el sexo. Los hombres que tienen problemas de obesidad también son más propensos a tener problemas para conseguir una erección.\n")
    respuesta = int(input(
        "1 - IMC 18.5 - 24.9\n"
        "2 - IMC 25.0 - 29.9\n"
        "3 - IMC > 30.0\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 4:\n",arrayPreguntasHombre[3],"\n")
    print("Las enfermedades de transmisión sexual (ETS) se han añadido a esta lista como uno de los principales causantes de infertilidad tanto en mujeres como en hombres. En el caso de los hombres estas enfermedades son las responsables de este problema en un 15 por cierto de los casos, ya que pueden interesar a las vías seminales, así como a los testículos y su capacidad para producir suficientes espermatozoides sanos, afectando negativamente al número, la movilidad, la morfología y la integridad del ADN.\n")
    respuesta = int(input(
        "1 - Nunca ha tenido una ETS\n"
        "2 - Si\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 5:\n",arrayPreguntasHombre[4],"\n")
    print("El abuso del alcohol, según diferentes estudios, puede incidir en un menor número de espermatozoides, de testosterona y en un aumento de estrógenos. Esto podría influir en una disminución de la libido o deseo sexual y disminución de la fertilidad. Esto es más obvio cuando ya tenemos un daño hepático. Respecto al uso de otras drogas, uno de los problemas más preocupantes es que además de provocar o agravar las disfunciones sexuales masculinas, al empeorar el estado general de salud, pueden dañar el ADN o material hereditario.\n")
    respuesta = int(input(
        "1 - No bebo alcohol ni uso drogas\n"
        "2 - Alcohol moderado o cualquier uso de drogas ocasional\n"
        "3 - Consumo intenso de alcohol o uso regular de drogas\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 6:\n",arrayPreguntasHombre[5],"\n")
    print("Las enfermedades como la diabetes, asma, alta presión arterial, artritis reumatoide u otras enfermedades serias pueden dificultar lograr el embarazo. Los medicamentos que se utilizan para tratar estas enfermedades pueden inhibir tu capacidad de concebir o ser dañinas para el bebé no nato.\n")
    respuesta = int(input(
        "1 - Ningún problema médico\n"
        "2 - Problema médico leve\n"
        "3 - Problema médico severo\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 7:\n",arrayPreguntasHombre[6],"\n")
    print("La quimioterapia (quimio) y/o la radiación funciona al eliminar las células en el cuerpo que se dividen rápidamente. Dado que los espermatozoides se dividen rápidamente, constituyen un blanco fácil para el daño causado por la quimioterapia. La infertilidad permanente puede surgir si todas las células inmaduras en los testículos que se dividen para producir nuevos espermatozoides (llamadas células madre espermatogonias) se dañan al punto que ya no pueden producir espermatozoides maduros.\n")
    respuesta = int(input(
        "1 - No\n"
        "2 - Ocasionalmente\n"
        "3 - Frecuente o en tratamientos de quimio o radioterapia\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 8:\n",arrayPreguntasHombre[7],"\n")
    print("El efecto del calor en la producción espermática ha sido fuertemente documentado a lo largo de los años. Hoy se sabe que puede llevar a la oligospermia -baja cantidad de espermatozoides en el eyaculado-, astenospermia – alteración en la función de los espermatozoides- y teratozoospermia – alteración en la forma de los espermatozoides.\n")
    respuesta = int(input(
        "1 - No\n"
        "2 - Ocasionalmente 1 vez al mes\n"
        "3 - Frecuentemente\n"
    ))
    total = total + respuesta
    os.system("pause")
    print("\n Pregunta 9:\n",arrayPreguntasHombre[8],"\n")
    print("El presentar dolor constante en la región testicular podría ser índice de varicocele, la presencia de venas varicosas o dilatadas en el escroto. Alrededor de 15 por ciento de los hombres padece esta enfermedad. Aunque para algunos no representa un problema, casi 40 por ciento de los hombres infértiles tiene varicocele. Es importante señalar que el varicocele izquierdo es más común que el derecho (alrededor de 80 por ciento de los casos).\n")
    respuesta = int(input(
        "1 - No\n"
        "2 - Ocasionalmente presento molestias o tengo diagóstico de varicocele\n"
        "3 - Molestia constante o diagnosticado con Varicocele de 3er grado\n"
    ))
    total = total + respuesta
    os.system("pause")

    #RESULTADOS HOMBRE
    print("RESULTADOS\n"
         "TU PUNTUACION ES DE :",total,"\n")
    if total <=12 :
        print("La recomendación general es intentar concebir con tu pareja durante un año utilizando un apoyo para predecir la ovulación de su pareja para ayudarle a la programación correcta del coito antes de buscar ayuda médica. Algunos tipos de apoyo para predecir la ovulación: Tiras de LH (hormona leutenizante), chequeo frecuente de la temperatura corporal de la mujer, cualquier app que indique los días fértiles de la mujer.\n")
    elif total > 12 and total <=18:
        print("La recomendación general es intentar concebir durante seis meses antes de buscar ayuda médica a menos que tenga un problema de fertilidad conocido, o más de 60 años; en cuyo caso puede ser buena idea consular a un especialista en fertilidad para obtener asesoría y una evaluación a la brevedad. Si alguno de sus puntos se deben a problemas por su estilo de vida, debe modificarlo de inmediato. Un buen recurso para obtener información acerca del estilo de vida es Fertility & Lifestyle (Fertilidad y Estilo de Vida). Idealmente los problemas de estilo de vida deben alterarse al comenzar a buscar la concepción, pero todos estos factores se vuelven progresivamente más importantes al involucrarse más en los tratamientos de fertilidad.\n")
    elif total >18:
        print("Es muy problable que tengas problemas de fertilidad o urológicos conocidos, y es altamente recomendable ver a un especialista en fertilidad a la brevedad.\n")
    #print("Resultado: ",total)

    print("\nLa infertilidad tiene solución, mediante un diagnóstico preciso y un tratamiento personalizado. Este test es solo sugerencia por lo cual no quiere "
    "decir que tengas el problema, acercate a una institucion para descartar dudas.\n")




    