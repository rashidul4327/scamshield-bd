# ScamShield BD - code

- `index.html` : the complete tool (open in any browser, works offline). Contains the rule engine, URL and sender checks, and the embedded ML model.
- `train.py` : retrain the ML layer with ONE command: `python train.py` (needs Python + scikit-learn). Reads `data.csv`, writes `model.json`, and embeds the model into `index.html`.
- `data.csv` : small SYNTHETIC seed dataset (label 1 = scam, 0 = normal). Add newly reported, anonymised messages as new rows, then run `python train.py`.
- `make_seed_data.py` : script that created the synthetic seed dataset.
- `model.json` : exported model (char n-gram TF-IDF + logistic regression).

Note: the seed data is synthetic and only tests the pipeline. Scores on it are not real-world accuracy.
