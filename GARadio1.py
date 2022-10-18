from pygame import mixer


chooseAlbum = str(input("Selecciona el album:\n 1. Zaba\n 2. How To Be a Human Being\n 3. Dreamland \n"))
chooseAlbum = chooseAlbum.lower()
if chooseAlbum == "zaba":
        album = 'zaba.mp3'

elif chooseAlbum == "htbahb":
        album = 'How_To_Be_A_Human_Being.mp3'

elif chooseAlbum == "dreamland":
        album = 'dreamland.mp3'


mixer.init()
mixer.music.load(album)
mixer.music.set_volume(0.7)
mixer.music.play()


while True:
    print("Pulsa p para detener reproduccón")
    print("Pulsa r para reanudar reproducción")
    #print("pulsa e para elegir album")
    print("Pulse s para salir")

    opcion = input(">")

    if opcion == "p":
        mixer.music.pause()
    elif opcion == "r":
        mixer.music.unpause()
   # elif opcion == "e":
    #    mixer.music.stop()
    elif opcion == "s":
        mixer.music.stop()
