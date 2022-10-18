from pygame import mixer

mixer.init()

album=str(input("Selecciona el album:\n 1. Zaba\n 2. How To Be a Human Being\n 3. Dreamland \n"))
    #añadimos la ruta
mixer.music.load(album)
mixer.music.set_volume(0.7)
mixer.music.play()




while True:
    print("Pulsa p para detener reproduccón")
    print("Pulsa r para reanudar reproducción")
    print("pulsa e para elegir album")
    print("Pulse s para salir")
    
    opcion = input(">")
    
    if opcion == "p":
        mixer.music.pause()
    elif opcion == "r":
        mixer.music.unpause()
    elif opcion == "e":
        mixer.musc.stop()
        album=str(input("Selecciona el album:\n 1. Zaba\n 2. How To Be a Human Being\n 3.Dreamland"))
        mixer.music.load(album)
        mixer.music.set_volume(0.7)
        mixer.music.play()
    elif opcion == "s":
        mixer.music.stop()
 
        
