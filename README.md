# TFG - Anàlisi i optimització d’embeddings en LLMs: Comparació entre models genèrics i ajustats

Aquest projecte de treball de fi de grau explora l'ús de **Large Language Models (LLM)** per representar la semàntica de fragments de textos matemàtics, mitjançant embeddings i tècniques de **fine-tuning contrastiu**. S’avalua com de bé aquests models poden distingir entre parelles de textos **semànticament similars** o **diferents** en un context altament tècnic.

---

## Objectius

- Avaluar la capacitat de models LLM per distingir semànticament fragments matemàtics.
- Aplicar **fine-tuning contrastiu** amb parelles etiquetades per millorar el rendiment.
- Comparar diferents models: preentrenats (AnswerDotAI, NomicAI) i fine-tuned.
- Visualitzar els resultats amb corbes ROC, matrius de confusió i UMAP.

```

## Estructura del projecte

TFG/
├── data/
│   ├── raw/                      # Dades originals (papers en .tar.gz)
│   └── papers_feb_2025.csv       # Llista de papers a processar
│
├── Projecte/
│   ├── Projecte_TFG_MartiMussons.docx
│   └── Projecte_TFG_MartiMussons.pdf
│
├── src_tex/
│   ├── data/
│   │   ├── output_tex/           # Conté fragments de text extrets
│   │   ├── extract_tex_from_tar_gz.py
│   │   └── parelles_prova.ipynb
│   │
│   ├── evaluation/               # Anàlisi de models
│   │   ├── answerdotai.ipynb
│   │   ├── nomicai.ipynb
│   │   └── parelles.csv          # Dataset etiquetat de parelles
│   │
│   ├── prova/                    # Experiments 
│   │   ├── output/
│   │   ├── parelles2.csv
│   │   ├── parelles3.csv
│   │   └── train2.ipynb
│   │
│   └── training/                 # Entrenament i resultats finals
│       ├── modernbert-contrastive-manual/
│       │   ├── model.safetensors, config.json, etc.
│       ├── analisi_errors.ipynb
│       ├── df_blocks.csv
│       ├── parelles.csv
│       ├── parelles_mal_classificades.csv
│       └── train_finetuned.ipynb
│
├── actica.ps1, entorn.ps1        # Scripts d'activació de l'entorn virtual
├── requirements.txt              # Llistat de llibreries Python necessàries
├── README.md                     # Aquest fitxer
└── .gitignore

---

## Models utilitzats

- [`answerdotai/ModernBERT-base`](https://huggingface.co/answerdotai/ModernBERT-base)
- [`nomic-ai/modernbert-embed-base`](https://huggingface.co/nomic-ai/modernbert-embed-base)
- Model contrastiu **fine-tuned** sobre corpus matemàtic propi (guardat a `training/modernbert-contrastive-manual/`)

```

## Resultats

S’ha observat una millora clara en les mètriques després del *fine-tuning*:

- **AUC ROC ≈ 0.999**
- **Accuracy ≈ 0.99**
- Clústers semàntics molt millor definits amb UMAP

---

## Comandes útils
### instalar dependencies requirements
pip install -r requirements.txt

### crear entorn virtual
.\entorn.ps1

### activar entorn visrtual
.\activa.ps1

---

## Autor
- Martí Mussons Marin
- Any 2025
- Universitat Autònoma de Barcelona 


