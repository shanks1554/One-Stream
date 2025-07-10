# 🎬 One Stream: Anime Recommendation System

One Stream is a smart anime recommendation system built with **Flask** (frontend) and **FastAPI** (backend). It helps users discover anime based on genres or by submitting a list of watched titles - powered by content-based filtering and natural language techniques.

---

## 🚀 Features

- 🌐 **Modern Frontend** using Flask with Jinja templates

- 🔍 **Explore by Genre** – select multiple genres to get personalized recommendations

- 📺 **Get Recommendations by Watched List** – enter titles you've watched, get suggestions

- 📄 **Anime Detail Pages** – full view of synopsis, score, genres, and more

- 🌀 **Smooth Animations & Responsive UI** – elegant modern UI/UX with autocomplete, transitions

- 📦 **Backend APIs via FastAPI** – fast, modular, and ready for scale

---

## 🗂️ Project Structure

```
onestream/
│
├── backend/             # FastAPI backend (ML recommendation logic)
│   ├── main.py
│   ├── meta.py
│   └── recommend.py
|
├── frontend/            # Flask frontend (templates, static files, routes)
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── config/              # Config files 
├── data/                # Processed anime data (CSV/JSON)
├── notebooks/           # Jupyter notebooks for development / EDA
├── run.py               # Launches both backend and frontend
├── requirements.txt     # Python dependencies
└── README.md            
```

---

## 🧪 How to Run Locally

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Both Servers
Use the provided script:

```bash
python run.py
```

This will:

- Start the **Flask** server (frontend)

- Start the **FastAPI** server (backend)

Access frontend at: `http://127.0.0.1:5000`  
FastAPI docs at: `http://127.0.0.1:8000/docs`

---

## 🤖 Recommendation Logic


- **Content-Based Filtering**: Computes cosine similarity between anime feature vectors

- **Features Used**: Title, synopsis, genres, popularity, studios

- **Preprocessing**: NLP techniques like TF-IDF and CountVectorizer

---

## 📊 Dataset

Cleaned and processed from multiple sources:

- [MyAnimeList](https://myanimelist.net/)

- Contains metadata: title, genres, synopsis, score, episodes, popularity, studios, etc.

---

## 📌 TODO / Bonus Features


- 🧠 Session caching for watched history

- 🕵️‍♂️ Recently viewed / continue watching bar

- 🌙 Dark/light mode toggle

- 📱 Fully responsive mobile UI



---

## 💻 Tech Stack

| Layer     | Stack        |
|-----------|--------------|
| Frontend  | Flask, Jinja, HTML, CSS, JS |
| Backend   | FastAPI, Python |
| ML / Data | Pandas, Scikit-learn, Cosine Similarity |
| UI/UX     | Custom CSS, Neumorphism, Animations |

---

## 📬 Contact

Built with ❤️ by **Deep(Shanks)**.

Feel free to fork, contribute, or reach out!
