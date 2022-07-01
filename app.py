import cv2

#Importando os dados para identificação dos rostos
dadosXML_rostos = 'haarcascade_frontalface_alt2.xml'

#Lendo o arquivo e populando o classificador
classificador_rosto = cv2.CascadeClassifier(dadosXML_rostos)

#Definindo/configurando a camera
camera = cv2.VideoCapture(0) #Inserir o ID da camera

#Definindo o tamanho da camera (quanto menor a imagem, melhor é o processamento)
camera.set(3, 640)#Width
camera.set(4, 480)#Height

#iniciando a captura da imagem pela camera
while not cv2.waitKey(20) == ord("q"):
    #pegando a captura da imagem no instante atual, um vídeo é uma sequência de imagens.
    verificador, imagem_colorida = camera.read()

    #Mudanço a cor da imagem para preto e branco
    imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

    #configurar para detectar o rosto
    rostos = classificador_rosto.detectMultiScale(imagem_cinza,)#definindo a imagem cinza por ser mais leve para processar

    #criar um retangulo nos rostos detectados
    for x,y,w,h in rostos:
        cv2.rectangle(imagem_colorida,(x,y), (x + w, y +h), (0,0,255),2)

    #exibindo as imagens na tela
    cv2.imshow('camera',imagem_colorida)

camera.release()#Encerrando a conexão com a camera


