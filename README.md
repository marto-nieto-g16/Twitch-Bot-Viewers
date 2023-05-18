# Twitch Bot Viewers

Un script de Python que utiliza Selenium para abrir múltiples sitios proxy y enviar vistas a un canal de Twitch

## Requisitos

- Python 3.x
- Selenium
- Colorama
- pystyle
- Chrome Web Driver

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/marto-nieto-g16/Twitch-Bot-Viewers.git
```

2. Instala las dependencias:

```
pip install selenium colorama pystyle
```

3. Descarga el Chrome Web Driver y coloca el archivo ejecutable en el mismo directorio que el script.

## Uso

1. Ejecuta el script:

```
python view.py
```

2. Ingresa el nombre de tu canal de Twitch cuando se te solicite.

3. Ingresa el número de sitios proxy que deseas abrir y usar para enviar vistas.

4. El script abrirá el número especificado de sitios proxy y enviará vistas a tu canal de Twitch.

5. Para detener el script, presiona `Ctrl + C` en la línea de comando.

Este sistema abre múltiples sitios en segundo plano, así que asegúrese de tener suficiente RAM o realice esta operación en una computadora que no esté en uso. (Podría estar en un potente servidor virtual).

Si la entrega de la audiencia tarda demasiado y envía solo a unos pocos espectadores, cierre el cliente y vuelva a abrirlo, luego repita los mismos pasos. (el proxy a veces puede ralentizarse).

Nota: El software diseñado para realizar pruebas de seguridad del sitio web. El autor no es responsable del uso ilegal de estos programas. Esto es 100% educativo, por favor no haga un mal uso de esta herramienta.

Si encuentras algún error, contacta al autor en Github.
