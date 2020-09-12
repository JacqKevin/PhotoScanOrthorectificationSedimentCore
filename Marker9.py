#!/usr/bin/env python
#-*- coding: utf-8 -*-
import Metashape # Ouverture
chunk = Metashape.app.document.chunk # D�tection du dossier de travail 
print("Detection des marqueurs")
chunk.detectMarkers(Metashape.TargetType.CircularTarget12bit,100) # d�tection des marqueurs
chunk.loadReference("C:/Users/edytem/Desktop/ASSEMBLAGES_PHOTOS_CAROTTES/MarkerBanc9.txt",Metashape.ReferenceFormatCSV) # Recherche des r�f�rences
chunk.updateTransform() # Sauvegarde
