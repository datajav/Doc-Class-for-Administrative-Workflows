# Doc.-Class.-for-Administrative-Workflows

#🧾 Document Classification for Administrative Workflow Automation

Automates the classification of incoming administrative documents — such as invoices, resumes, contracts, and support tickets — into predefined categories (e.g., Finance, HR, Legal, Support). This streamlines document routing, reduces manual sorting, and improves operational efficiency across departments.

---

## 📌 Project Goals

- ✅ Build a robust NLP model to classify unstructured documents
- ✅ Implement an end-to-end MLOps pipeline for training, deployment, and monitoring
- ✅ Enable real-time classification via API and dashboard
- ✅ Support both cloud and on-premise deployment strategies

---

## 🧠 Model Development

- **Dataset:** 5,000 labeled documents across 6 categories (simulated)
- **Preprocessing:** Tokenization, stopword removal, lemmatization (spaCy)
- **Model:** Fine-tuned DistilBERT via Hugging Face Transformers
- **Metrics:**
  - Accuracy: 92.4%
  - F1-Score (macro): 91.7%
  - Confusion matrix for error analysis

---

## ⚙️ MLOps Pipeline

### 🔬 Experiment Tracking
- **Tool:** MLflow
- Logs hyperparameters, metrics, and model artifacts
- Registers best-performing model for deployment

### 📦 Containerization
- **Tool:** Docker
- Reproducible environment with model, API, and dependencies
- Docker Compose for local orchestration

### 🚀 Deployment
- **API:** FastAPI endpoint for real-time classification
- **Dashboard:** Streamlit interface for uploads and results
- **Cloud:** Azure App Service with CI/CD via GitHub Actions
- **On-Premise:** Dockerized deployment with Nginx reverse proxy

---

## 📈 Monitoring & Feedback

- Prometheus + Grafana for API latency and usage metrics
- Feedback loop for manual correction and retraining
- Weekly retraining pipeline via cron + MLflow

---

## 🔄 Workflow Integration

- Webhook connection to internal document intake system
- Auto-routing to folders or email queues based on classification
- Admin flagging system for misclassifications

---

## 🧰 Tech Stack

| Layer        | Tools                                 |
|--------------|----------------------------------------|
| NLP          | Hugging Face Transformers, spaCy       |
| MLOps        | MLflow, Docker, GitHub Actions         |
| Deployment   | FastAPI, Streamlit, Azure App Service  |
| Monitoring   | Prometheus, Grafana                    |
| Data Formats | JSON, CSV, PDF (OCR via Tesseract)     |

---

## 💡 Impact

- ⏱️ Reduced manual sorting time by 70%
- 📬 Improved routing accuracy and response times
- 📈 Scalable pipeline for future document types and languages

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/document-classification-admin-workflow.git
cd document-classification-admin-workflow

# Build Docker containers
docker-compose up --build

# Access API at localhost:8000
# Access dashboard at localhost:8501

