# P1-IntroRPi-PWM
## 1.Introducción
La Raspberry Pi puede proporcionar una amplia gama de automatización y procesamiento de datos. Sus principales aplicaciones son aquellas en las que se utilizan los diferentes sensores y se convierten los datos para utilizarlos y controlar los dispositivos a experimentar durante el curso.

## 2. Descripción de la placa
En la placa nos podemos encontrar 8 elementos y conectores diferentes:
1. **Puertos GPIO**: se pueden leer valores de cualquier periférico así como enviar los valores. También se pueden conectar LEDs (como en esta primera práctica) o pantallas LCD.
2. **Conector de salida de audio de 3,5mm**
3. **USB**
4. **Ethernet**: proporciona conexión a Internet por cable.
5. **Conector de cámara CSI**
6. **Conector HDMI**
7. **Micro USB**: se necesita un voltaje de entrada de 5V y un mínimo de 2,5A.
8. **Ranura para microSD**: lugar donde la Raspberry tiene instalado su sistema operativo además de donde se almacenará todos los documentos, programas...

![Elementos e interfaz](https://github.com/rsanchez2021/Image/blob/main/interfazRaspberryPi.jpg "Elementos e interfaz")

Esta misma imagen se puede ver con facilidad en el terminal con el comando **pinout**
![Pinout en terminal](

## 3. Instalación del Sistema Operativo
Para instalarlo necesitamos la tarjeta microSD. En ella hay que descargar e instalar una imagen del sistema operativo, en este caso: Raspberry Pi OS. Primero hay que formatear la microSD con la herramienta de Discos de Linux. Como usuario y contraseña utilizaremos los mencionados en la guía de la práctica.

## 4. Introducción a la técnica PWM
Todos los pines GPIO de la Raspberry Pi son **digitales**, de decir, la conexión de un LED a cualquier pin GPIO, solo nos va a permitir encenderlo o apagarlo. Para poder controlar el brillo del LED como una señal analógica hace falta utilizar la PWM, simulando voltajes analógicos a través de los pines digitales. **Los pines GPIO son de 3,3V**, pero si queremos inyectar una señal de 1,65V hemos de encender y apagar el pin de forma que esté encendido la mitad del tiempo y la otra mitad apagado. Si queremos simular una salida del 1,1V deberíamos tomar tiempo para que estuviera encendida el 33%.

## 5. Instalación del LED
Conexiones de un LED con la placa Raspberry Pi:

![Conexiones del LED](https://github.com/rsanchez2021/Image/blob/main/LED.PNG "Conexión LED")

En la siguiente imagen podemos ver cómo se ha conectado el LED a la placa para esta primera práctica:

![Primer circuito](https://github.com/rsanchez2021/Image/blob/main/p1.PNG "Disposición del LED")

## 6. Manejo básico del LED mediante terminal
```bash
echo 17 > /sys/class/gpio/export #inicializar el fichero del puerto GPIO 17 // puerto 11
echo out > /sys/class/gpio/gpio17/direction #especificar su uso como salida
echo 1 > /sys/class/gpio/gpio17/value #encender el LED
echo 0 > /sys/class/gpio/gpio17/value #apagar el LED
echo 17 > sys/class/gpio/unexport #resetear el pin borrando el fichero 
```

## 7. Programación del LED mediante PWM
```python
import RPI.GPIO as GPIO #importar la biblioteca Rpi

GPIO.setmode (GPIO.BOARD) #indicar esquema de numeración de pines
GPIO.setup (11, GPIO.OUT) #indica el pin a utilizar y el uso, el 11 de salida
pwn = GPIO.PWM (11,100) #creamos PWM con el pin y la frecuencia de trabajo
pwm.start (50) #porcentaje del periodo de la señal en estado alto

input (“ Ejecutando hasta que pulse una tecla”) #fuerza a para la ejecución del programa
pwm.stop ()
GPIO.cleanup ()
```
En caso de querer cambiar el ciclo de trabajo,teniendo en cuenta que el máximo es 100 (100%), se puede hacer utilizando el comando: 
```python
pwm.ChangeDutyCycle (1)
```
Por otro lado, si queremos  cambiar la frecuencia se puede hacer con el comando:
```python
pwm.ChangeFrequency (1000)
```

Por último, es importante que al ejecutar el programa desde la terminal se utilice **python3**
```bash
python3 LED.py
```
