Predicția Adicției față de Smartphone
Am ales această temă deoarece utilizarea excesivă a smartphone-ului a devenit o problemă globală, afectând direct nivelul de stres și calitatea somnului.
Analizând variabile precum timpul petrecut pe rețelele sociale, numărul de notificări și impactul asupra somnului, 
modelul va putea anticipa dacă un utilizator prezintă un risc ridicat de adicție.

**Sursa:** [Kaggle] https://www.kaggle.com/datasets/zahranusratt/smartphone-usage-and-addiction-analysis-dataset?resource=download
**Data descărcării:** 13 Aprilie 2026

##  Tehnologii utilizate:
* **Limbaj de programare:** Python
* **Principalele biblioteci folosite:**
  * `pandas` – pentru încărcarea, curățarea și transformarea datelor brute.
  * `scikit-learn` – pentru antrenarea modelelor (`DecisionTree`, `RandomForest`, `LogisticRegression`) și optimizarea parametrilor cu `GridSearchCV`.
  * `matplotlib` & `seaborn` – pentru analiza grafică (Matricea de corelație și graficele de impact).

##  Structura depozitului:
* 📄 `main.py` — codul sursă pentru curățarea datelor, antrenarea algoritmilor și salvarea rezultatelor.
* 📊 `smartphoneusage.csv` — Setul de date brut în format tabelar care conține înregistrările comportamentale ale utilizatorilor.
* 📓 `smartphoneusage.ipynb` — Notebook-ul Jupyter utilizat pentru analiza datelor, testarea graficelor/matricea de corelație.
