"""
Trier les fichiers contenus dans le dossier selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif, flv, wmv, mov, wav, m4a, m4v, f4v, f4a, m4b, m4r : Videos
bmp, png, jpg, jpeg, svg : Images
txt, pptx, csv, xls, odp, pages, pdf, doc, odt, xls  : Documents
autres : Divers
"""
from pathlib import Path


EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".flac": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".m4a": "Videos",
                      ".m4v": "Videos",
                      ".f4v": "Videos",
                      ".f4a": "Videos",
                      ".m4b": "Videos",
                      ".m4r": "Videos",
                      ".mov": "Videos",
                      ".wmv": "Videos",
                      ".flv": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".jepg": "Images",
                      ".svg": "Images",
                      ".txt": "Documents",
                      ".pdf": "Documents",
                      ".doc": "Documents",
                      ".odt": "Documents",
                      ".pptx": "Documents",
                      ".xls": "Documents",
                      ".docx": "Documents",
                      ".csv": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents"}

BASE_DIR = Path('C:/Users/Admin/Downloads')


files = [f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:
    dossier_cible = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    dossier_cible_absolu = BASE_DIR / dossier_cible
    dossier_cible_absolu.mkdir(exist_ok=True)
    fichier_cible = dossier_cible_absolu / file.name
    file.rename(fichier_cible)