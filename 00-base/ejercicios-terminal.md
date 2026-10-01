.# Ejercicios de terminal (PowerShell)

Cinco ejercicios cortos para practicar los comandos de `notas-terminal.md`, ordenados de más fácil a más difícil.
Intenta hacerlos sin mirar las soluciones del final.

---

## Ejercicio 1: ¿Dónde estoy?

1. Abre una terminal de PowerShell.
2. Averigua en qué carpeta estás.
3. Mira qué hay dentro de esa carpeta.
4. Vete a tu carpeta de casa y comprueba que has llegado.

## Ejercicio 2: Subir y bajar

1. Desde tu carpeta de casa, baja a la carpeta `proyectos-ia` y luego a `00-base`. Usa **Tab** para completar los nombres en vez de escribirlos enteros.
2. Comprueba dónde estás.
3. Sube un nivel y comprueba de nuevo dónde estás.
4. Escribe `cd` solo, sin destino, y fíjate en qué pasa (o en qué no pasa).

## Ejercicio 3: Tu primera carpeta con archivos

1. Dentro de `00-base`, crea una carpeta llamada `practica-terminal` (recuerda: sin espacios, con guiones).
2. Entra en ella.
3. Crea dos archivos vacíos: `notas.txt` e `ideas.md`.
4. Lista el contenido para comprobar que los dos archivos están ahí.

## Ejercicio 4: Crear y borrar carpetas

1. Dentro de `practica-terminal`, crea dos carpetas: `borrador` y `final`.
2. Lista el contenido para ver que están.
3. Borra la carpeta `borrador`.
4. Vuelve a listar para comprobar que ya no está.
5. Pregunta para pensar: si te equivocas y borras la carpeta que no era, ¿puedes recuperarla de la papelera?

## Ejercicio 5: Mini proyecto completo

Sin mirar los ejercicios anteriores, haz todo esto seguido:

1. Vete a tu carpeta de casa.
2. Llega hasta `proyectos-ia\00-base\practica-terminal` usando Tab.
3. Crea una carpeta `mi-web` y entra en ella.
4. Crea dentro un archivo `index.html` y una carpeta `imagenes`.
5. Comprueba con un comando que estás en `mi-web` y con otro que tienes el archivo y la carpeta.
6. Abre VS Code en esa carpeta.
7. Vuelve a la terminal, sube dos niveles y comprueba que estás en `00-base`.

---
---

# Soluciones

### Solución 1

```powershell
pwd
ls
cd ~
pwd
```

### Solución 2

```powershell
cd proyectos-ia     # escribe "cd pro" y pulsa Tab
cd 00-base          # escribe "cd 00" y pulsa Tab
pwd
cd ..
pwd                 # ahora estás en proyectos-ia
cd                  # no hace nada: sigues en el mismo sitio
```

### Solución 3

```powershell
mkdir practica-terminal
cd practica-terminal
ni notas.txt
ni ideas.md
ls
```

### Solución 4

```powershell
mkdir borrador
mkdir final
ls
rmdir borrador
ls
```

Respuesta a la pregunta: **no**. `rmdir` no manda la carpeta a la papelera, se borra directamente. Por eso conviene hacer `ls` antes de borrar y revisar bien el nombre.

### Solución 5

```powershell
cd ~
cd proyectos-ia\00-base\practica-terminal   # usa Tab en cada tramo
mkdir mi-web
cd mi-web
ni index.html
mkdir imagenes
pwd
ls
code .
cd ..
cd ..
pwd                 # deberías estar en 00-base
```

Truco extra: si algún comando se queda "colgado" ejecutándose, pulsa **Ctrl + C** para pararlo.
