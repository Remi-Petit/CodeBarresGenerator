from django.http import HttpResponse
from django.template import loader

import os

# Code-barres à 12 chiffres
from barcode import EAN13
# Code-barres à 10 chiffres
from barcode import Code128
# Code-barres à 10 chiffres
from barcode import Code39
from barcode.writer import ImageWriter


def index(request):
    template = loader.get_template("pageGenerator/index.html")
    context = {
    }
    return HttpResponse(template.render(context, request))

def codeBarre(request):
    if request.method == 'POST':
        numero_de_depart = request.POST.get('numero_de_depart', "")
        quantite = int(request.POST.get('quantite', ""))

        image_path = "./pageGenerator/static/pageGenerator/images/code-barre/"

        deleteImagesCodesBarres(request, image_path)

        liste_code_barre = []
        liste_code_barre_formate = []

        print(0.6 * 96 / 2.54)
        
        for i in range(0,quantite):
            numero_code_barre = str(int(numero_de_depart) + i)
            while len(numero_code_barre) < 6:
                numero_code_barre = "0" + numero_code_barre

            numero_image = "0003"+numero_code_barre

            # Générer le code-barres
            ean = Code128(numero_image, writer=ImageWriter())
            # Configurer le writer pour ne pas afficher le texte en dessous
            options = {
                'write_text': False
            }
            # Sauvegarder le code-barres dans un fichier
            filename = ean.save(image_path + numero_image, options)
            # Ajouter le code-barres dans un tableau
            liste_code_barre.append([numero_image,format_code_with_spaces(numero_image)])

            liste_code_barre_formate.append(format_code_with_spaces(numero_image))

    template = loader.get_template("pageGenerator/code-barres.html")
    context = {
        "numero_de_depart": numero_de_depart,
        "liste_code_barre": liste_code_barre,
        "quantite": quantite,
    }
    return HttpResponse(template.render(context, request))



def deleteImagesCodesBarres(request, image_path):
    # Supprimer toutes les images du dossier
    for filename in os.listdir(image_path):
        file_path = os.path.join(image_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def format_code_with_spaces(code):
    """Formate le code en ajoutant des espaces aux bons endroits."""
    return f"{code[0]} {code[1:4]} {code[4:7]} {code[7:]}"