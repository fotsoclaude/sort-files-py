"""
Trier les fichiers contenus dans le dossier selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
"""
from pathlib import Path


EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
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