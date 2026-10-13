# jose solis NC = 1472

# jose solis NC = 1472

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
# .parent nos ubica en 'exa-va-1472' desde 'codigopy-1472'
try:
    carpeta_proyecto = Path(__file__).resolve().parent.parent
except NameError:
    carpeta_proyecto = Path.cwd()

# Se actualizó el nombre de la imagen a 'img-camello-1472.png'
ruta_original = (
    carpeta_proyecto
    / "img-original-1472"
    / "img-camello-1472.png"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-1472"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img1472 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img1472 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen en la ruta: {ruta_original}\n"
        f"Verifica la ubicación del archivo 'img-camello-1472.png'."
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_1472 = cv2.rotate(
    img1472, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img1472.shape[:2]
centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_1472 = cv2.warpAffine(
    img1472,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho y 500 píxeles de alto
img600x500_1472 = cv2.resize(
    img1472, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200 píxeles
img_camello_1472 = img1472.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_camello_1472,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con ventanas redimensionables
titulos = [
    ("Camello Original 1472", img1472),
    ("Camello Rotado 90deg 1472", img90_1472),
    ("Camello Rotado 45deg 1472", img45_1472),
    ("Camello 600x500 1472", img600x500_1472),
    ("Camello con Rectangulo 1472", img_camello_1472)
]

# Definir el tamaño deseado para la ventana en pantalla (ancho, alto)
ancho_win, alto_win = 400, 300

for titulo, img in titulos:
    cv2.namedWindow(titulo, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(titulo, ancho_win, alto_win)
    cv2.imshow(titulo, img)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-camello1-1472.png"),
    img90_1472
)

cv2.imwrite(
    str(carpeta_resultados / "img-camello2-1472.png"),
    img45_1472
)

cv2.imwrite(
    str(carpeta_resultados / "img-camello3-1472.png"),
    img600x500_1472
)

cv2.imwrite(
    str(carpeta_resultados / "img-camello4-1472.png"),
    img_camello_1472
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas exitosamente.")
print("Presiona una tecla con las ventanas seleccionadas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("programa realizado por jose solis nc 1472")