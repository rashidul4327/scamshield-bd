"""ScamShield BD - retrain the ML layer with ONE command:   python train.py
Reads data.csv (columns: label,text ; 1 = scam, 0 = normal), trains
char n-gram TF-IDF + logistic regression (scikit-learn), writes model.json
and embeds the model into index.html so the page keeps working offline."""
import csv, json, re, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def normalize(s):   # must match normalize() in index.html
    d = {"০":"0","১":"1","২":"2","৩":"3","৪":"4","৫":"5","৬":"6","৭":"7","৮":"8","৯":"9"}
    return re.sub("[\u200c\u200d]","",re.sub("[০-৯]",lambda m:d[m.group()],s)).strip()

rows = list(csv.DictReader(open("data.csv", encoding="utf-8")))
X = [normalize(r["text"]) for r in rows]; y = [int(r["label"]) for r in rows]

vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(2,4), sublinear_tf=True,
                      min_df=2, max_features=4000)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
clf = LogisticRegression(C=4, max_iter=2000, class_weight="balanced")
clf.fit(vec.fit_transform(Xtr), ytr)
print("Seed-data check only (synthetic, NOT real-world accuracy): %.3f" % clf.score(vec.transform(Xte), yte))

# final model on all data
Xall = vec.fit_transform(X); clf.fit(Xall, y)
vocab = sorted(vec.vocabulary_, key=vec.vocabulary_.get)
model = {"ngram":[2,4], "vocab":vocab,
         "idf":[round(float(v),4) for v in vec.idf_],
         "coef":[round(float(v),4) for v in clf.coef_[0]],
         "bias":round(float(clf.intercept_[0]),4),
         "note":"Trained on a small synthetic seed dataset to test the pipeline."}
js = json.dumps(model, ensure_ascii=False, separators=(",",":"))
open("model.json","w",encoding="utf-8").write(js)

html = open("index.html", encoding="utf-8").read()
new = re.sub(r"/\*MODEL_START\*/.*?/\*MODEL_END\*/", lambda m:"/*MODEL_START*/const MODEL="+js+";/*MODEL_END*/", html, flags=re.S)
open("index.html","w",encoding="utf-8").write(new)
print("model.json written and embedded into index.html (%d terms, %d KB)" % (len(vocab), len(js)//1024))
