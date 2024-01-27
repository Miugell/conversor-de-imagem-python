from PIL import Image
from docx2pdf import convert
import os

extensoes = ["png", "jpg", "docx", "pdf"]
              #!0      1      2       3

def conversor(nome_arquivo):  
    nome = nome_arquivo.split(".")
    nome_do_arquivo = nome[0]
    extensao_do_arquivo = nome[1]

    if extensao_do_arquivo in extensoes:
        if extensao_do_arquivo == "png":
            imagem = Image.open(f"./image/{nome_do_arquivo}.png")
            imagem = imagem.convert("RGB")
            imagem.save(f"./convertidas/{nome_do_arquivo}.jpg")
        elif extensao_do_arquivo == "jpg":
            imagem = Image.open(f"./image/{nome_do_arquivo}.jpg")
            imagem = imagem.convert("RGBA")
            imagem.save(f"./convertidas/{nome_do_arquivo}.png")
        elif extensao_do_arquivo == "docx":
            caminho_documento = "./documentos/" + nome_do_arquivo + ".docx"
            convert(caminho_documento, "./convertidas/" + nome_do_arquivo + ".pdf" )
        else:
            caminho_documento = "./documentos/" + nome_do_arquivo + ".pdf"
            convert(caminho_documento, "./convertidas/" + nome_do_arquivo + ".docx")
    else:
        print('Extensão não disponível')

convertidas = "./convertidas"
image = "./image"
documentos = "./documentos"
document = os.listdir(documentos)
arquivos = os.listdir(image)


for arquivo in arquivos:
    conversor(arquivo)

for documento in document:
    conversor(documento)