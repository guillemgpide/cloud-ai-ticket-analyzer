# Cloud-AI Support Ticket Analyzer

[![Language](https://img.shields.io/badge/Language-Python_3.10+-blue.svg)](#)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](#)
[![Machine Learning](https://img.shields.io/badge/AI-Scikit_Learn_%7C_Pandas-FF9900.svg)](#)
[![Frontend](https://img.shields.io/badge/UI-Tailwind_CSS-38B2AC.svg)](#)

> An end-to-end Machine Learning web application that automatically categorizes customer support tickets and analyzes user sentiment. Features a custom data-generation pipeline, a trained NLP model (TF-IDF + Naive Bayes), and a responsive Single Page Application (SPA) UI.

## 🚀 Overview

This project simulates a modern AI-driven support desk. Instead of relying on rigid hardcoded rules, the core intelligence is powered by a **Multinomial Naive Bayes** classifier trained on dynamically generated data. The architecture follows MLOps best practices, separating the data generation, model inference, and API routing.

**Key Features:**
* **Automated Data Pipeline (`pandas`):** A custom Python script generates hundreds of varied support tickets with distinct categories and sentiments, eliminating data bias and enabling easy model scaling.
* **Real-time ML Inference (`scikit-learn`):** Vectorizes incoming text via TF-IDF and predicts the ticket's target department (`Technical`, `Billing`, `Sales`, `Support`, `Feedback`) alongside emotional sentiment.
* **Asynchronous REST API (`FastAPI`):** High-performance backend processing user requests and delivering JSON payloads.
* **Modern SPA Frontend (`Tailwind CSS` + Vanilla JS):** A clean, frictionless user interface embedded directly into the API, featuring asynchronous loading states and DOM manipulation without page reloads.

## 🏗️ Project Architecture

```text
cloud-ai-ticket-analyzer/
├── app/
│   └── main.py              # FastAPI server & HTML/JS Frontend injection
├── model/
│   └── classifier.py        # ML logic: loads CSV, trains model, predicts
├── data/                    # (Git-ignored) Generated datasets live here
├── Dockerfile               # Containerization blueprint
├── generar_dataset.py       # Data Augmentation script (Pandas)
└── requirements.txt         # Project dependencies
```

## ⚙️ Quick Start (Local Development)

1. **Clone the repository & setup environment:**
    ```bash
    git clone [https://github.com/yourusername/cloud-ai-ticket-analyzer.git](https://github.com/yourusername/cloud-ai-ticket-analyzer.git)
    cd cloud-ai-ticket-analyzer
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Generate the Training Dataset:**
    Run the data augmentation pipeline to create the `dataset.csv` file. This step is required before starting the API.
    ```bash
    python generar_dataset.py
    ```

3. **Launch the Application:**
    Start the FastAPI server. The ML model will automatically train itself on the generated dataset during startup.
    ```bash
    uvicorn app.main:app --reload
    ```

4. **Access the Application:**
    * **Web UI (Frontend):** Navigate to `http://localhost:8000`
    * **API Docs (Swagger UI):** Navigate to `http://localhost:8000/docs`

## 📦 Docker Deployment

To build and run the application inside a lightweight, isolated Docker container:

```bash
docker build -t ai-ticket-analyzer .
docker run -p 8000:8000 ai-ticket-analyzer
```