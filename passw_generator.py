#Importamos las dos librerias que nos ayudaran a usar valores aleatorios y a manejar cadenas de textos. Ademas de añadir colores.
import random;
import string;
import time;
import pyperclip;
from colorama import init, Fore, Style;

init(autoreset=True);

#Creamos variables donde guardamos los valores que utilizaran nuestras contraseñas.
minusculas=string.ascii_lowercase;
mayusculas=minusculas.upper();
numeros=string.digits;
simbolos=string.punctuation;

#Necesitaremos la base de la contraseña y la longitud que querramos darle.
base_contraseña=minusculas+mayusculas+numeros+simbolos;
longitud_contraseña=int(input(Fore.RED + Style.BRIGHT + 'Ingrese la cantidad de dígitos que requiera su contraseña: '));

#Usamos la funcion de random para mostrar y guardar la contraseña en la variable "look-passw".
look_passw=random.sample(base_contraseña,longitud_contraseña);

#Por último la presentamos a través de un string con el metodo .join() agregando la contraseña creada anteriormente.
passw_message ='Su contraseña es: '; 
passw_generada=''.join(look_passw);

#Utilizamos la libreria de pyperclip para copiar la contraseña al portapapeles.
pyperclip.copy(passw_generada);
#Mostramos la contraseña en nuestra consola despúes de 3 segundos.
tiempo_de_espera_passw = 3;
print(Fore.LIGHTBLUE_EX + f"Generando Contraseña, Por Favor Espere {tiempo_de_espera_passw} segundos :)")
time.sleep(tiempo_de_espera_passw);

print(passw_message + Fore.GREEN + Style.BRIGHT + passw_generada);

tiempo_de_espera_confirmacion_copiado = 2;
time.sleep(tiempo_de_espera_confirmacion_copiado);
print(Fore.MAGENTA + Style.BRIGHT + 'Copiamos su contraseña al portapapeles, ya puede pegarla donde lo necesite.')

tiempo_de_espera_msg= 2;
time.sleep(tiempo_de_espera_msg);
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"Gracias!!")