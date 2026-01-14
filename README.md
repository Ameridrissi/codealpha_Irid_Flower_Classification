# codealpha_Irid_Flower_Classification

### 2. Project Description

This project is a complete **machine learning classification system** for predicting Iris flower species (**Setosa, Versicolor, Virginica**) using the Iris dataset.
It includes:

* Model training and testing
* A Streamlit web application
* Deployment-ready configuration (Docker)

---

### 3. Project Structure

```
codealpha_IRISS_FLOWER_Classification/
│
├── Projet_WebApp_Streamlit/
│   ├── Modélisation/
│   │   ├── train.py        # Model training script
│   │   ├── test.py         # Model evaluation script
│   │   └── modeltree       # Saved trained model
│   │
│   ├── StreamlitWebApp/
│   │   ├── app.py          # Streamlit application
│   │   └── modeltree       # Model used by the app
│   │
│   ├── Déploiement/
│   │   ├── app.py          # Deployment-ready Streamlit app
│   │   ├── Dockerfile      # Docker configuration
│   │   └── requirements.txt
│   │
│   ├── Streamlit_app.txt   # Streamlit execution notes
│   └── Commandes utils.txt # Useful commands
│
└── README.md
```

---

### 4. Dataset

* **Name:** Iris Dataset
* **Features:**

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width
* **Target Classes:**

  * Setosa
  * Versicolor
  * Virginica

---

### 5. Machine Learning Workflow

1. Data loading and preprocessing
2. Model training (`train.py`)
3. Model testing (`test.py`)
4. Model persistence (`modeltree`)
5. Integration into Streamlit interface

---

### 6. How to Run the Project

#### A. Run the Streamlit App (Local)

```bash
pip install -r requirements.txt
streamlit run app.py
```

(Use the `app.py` inside **StreamlitWebApp** or **Déploiement**)

---

#### B. Train the Model

```bash
python train.py
```

Location:

```
Projet_WebApp_Streamlit/Modélisation/
```

---

#### C. Test the Model

```bash
python test.py
```

---

### 7. Deployment (Docker)

The project includes a **Dockerfile** for deployment.

```bash
docker build -t iris-streamlit-app .
docker run -p 8501:8501 iris-streamlit-app
```

Access the app at:

```
http://localhost:8501
```

---

### 8. Technologies Used

* Python
* Scikit-learn
* Streamlit
* Pandas / NumPy
* Docker

---

### 9. Use Cases

* Machine Learning demonstration
* Streamlit web app example
* Educational ML project
* Model deployment practice

---
