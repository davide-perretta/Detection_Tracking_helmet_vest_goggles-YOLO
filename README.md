# Detection_Tracking_helmet_vest_goggles-YOLO
Questo repository permette la detection con YOLOv5 e YOLOv7 di persone, elmetti, pettorine alta visibiltà e occhiali da lavoro, consente inoltre di effettuare il tracking delle persone. Saranno presenti gli script utilizzati per il "refaining" del dataset, saranno spiegati tutti i passaggi per ripetere il progetto e infine ci saranno i link ai dataset originali.

Link per scaricare i 4 dataset utilizzati:

  https://github.com/njvisionpower/Safety-Helmet-Wearing-Dataset

  https://public.roboflow.com/object-detection/hard-hat-workers

  https://github.com/MinhNKB/helmet-safety-vest-detection

  https://figshare.com/articles/dataset/CHVG_Dataset/19625166

Dopo aver scaricato i 4 dataset si possono unire, cosí da ottenere un unico dataset. Successivamente si deve utilizzare lo script "detect_and_remove.py", attraverso questo script ci sará l'eliminazione di tutte le immagini duplicate. Successivamente si puó usare "Convert_xml2yolo.py" per convertire le etichette dal formato Pascal VOC al formato YOLO.

Per poter addestrare il modello di YOLOv7 é necessario prima scaricare tutte le dipendenze dal file "requirements.txt"

Nella cartella "helmet_vest_goggles_detection_v7" è presente il modello addestrato in YOLOv7 al rilevamento di persone elmetti, pettorine alta visibiltà e occhiali. É presente un file "requirements.txt" per poter scaricare tutte le dipendenze di YOLOv7. Per effettuare il training personalizzato con un nuovo dataset, si deve utilizzare lo script python "train.py" e specificare i parametri (si possono vedere nel file train.py dal rigo 529 al rigo 564). Mentre se si vuole effettuare la detection si deve usare lo script "detect.py" (controllare anche qui i parametri che si possono specificare) ed è possibile utilizzare il peso già addestrato "helmet_vest_goggles_v7.pt". Nella cartella sono presenti anche degli esempi di detection. Inoltre per effettuare il test del modello si deve usare lo script "test.py" e specificare come parametro "--task test".

Nella cartella "helmet_vest_goggles_detection_v5" è presente il modello allenato in YOLOv5 e anche qui è presente un file "requirements.txt" per poter scaricare tutte le dipendenze di YOLOv5. Questo modello a differenza di YOLOv7 non è molto preciso nella detection, quindi è sconsigliabile utilizzarlo. Però si può effettuare il training dei dati personalizzati, sempre attraverso lo script "train.py" e si può effettuare la detection con "detect.py". Si possono anche effettuare i test con lo script "val.py" e anche in questo caso è necessario specificare il parametro "--task test". Anche in questa cartella ci sono degli esempi di detection in YOLOv5.

Nella cartella "Tracking" è presente il tracker per YOLOv5 e YOLOv7, in questo funziona solo per YOLOv7 perchè ha tutti i file necessari. Per farlo funzionare anche per YOLOv5 si deve aggiungere i file di YOLOv5 nella cartella "YOLOv5". Per effettaure il tracking delle persone in YOLOv7 si deve usare lo script "track_v7.py". Sono presenti degli esempi per vedere il funzionamento del tracker.


