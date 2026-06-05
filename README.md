# Financial AI Platform 🤖💼

An agentic AI platform for financial document analysis, risk assessment, and executive reporting using cutting-edge technologies like **CrewAI**, **LangGraph**, **OpenAI**, and **FAISS**.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

The Financial AI Platform is an intelligent system designed to analyze financial documents, assess business risks, and generate comprehensive executive reports. It leverages multiple AI agents working together (via CrewAI) to perform specialized tasks in financial analysis.

### Key Capabilities:
- **Document Analysis**: Extract and analyze financial data from various document formats
- **Risk Assessment**: Identify and evaluate financial and operational risks
- **Executive Reporting**: Generate professional reports with actionable insights
- **Vector-based Search**: Fast and intelligent document retrieval using FAISS
- **Agentic Workflow**: Multi-agent system for complex financial analysis tasks

---

## ✨ Features

- ✅ Multi-agent AI system powered by CrewAI
- ✅ Advanced document processing and analysis
- ✅ Risk assessment and mitigation recommendations
- ✅ Executive summary generation
- ✅ Vector database integration (FAISS) for semantic search
- ✅ OpenAI GPT integration for intelligent analysis
- ✅ LangGraph for complex workflow orchestration
- ✅ RESTful API endpoints
- ✅ Scalable architecture

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core programming language |
| **CrewAI** | Multi-agent orchestration framework |
| **LangGraph** | Workflow and graph-based task execution |
| **OpenAI API** | Large language model for analysis |
| **FAISS** | Vector similarity search and indexing |
| **FastAPI** | REST API framework |
| **Pydantic** | Data validation and settings management |
| **Python-dotenv** | Environment configuration |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Git**
- **OpenAI API Key** (from [platform.openai.com](https://platform.openai.com))

### System Requirements:
- RAM: Minimum 4GB (8GB recommended)
- Storage: At least 2GB free space
- OS: Windows, macOS, or Linux

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/drdeveloper88/financial-ai-platform.git
cd financial-ai-platform
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import crewai; import faiss; print('Installation successful!')"
```

---

## ⚙️ Configuration

### Step 1: Create Environment File

Create a `.env` file in the project root directory:

```bash
touch .env
```

### Step 2: Add Configuration Variables

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7

# Application Settings
LOG_LEVEL=INFO
DEBUG=False

# Database/Vector Store
VECTOR_DB_PATH=./data/vector_store
FAISS_INDEX_PATH=./data/faiss_index

# API Settings
API_PORT=8000
API_HOST=0.0.0.0
```

### Step 3: Obtain OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Create an account or log in
3. Navigate to API keys section
4. Generate a new API key
5. Copy and paste it in your `.env` file

---

## 🚀 Usage

### Basic Usage

#### 1. Analyze Financial Documents

```python
from financial_ai_platform import FinancialAnalyzer

analyzer = FinancialAnalyzer()

# Upload and analyze a document
result = analyzer.analyze_document(
    file_path="path/to/financial_document.pdf",
    analysis_type="full_analysis"
)

print(result)
```

#### 2. Generate Risk Assessment

```python
from financial_ai_platform import RiskAssessor

assessor = RiskAssessor()

# Perform risk assessment
risk_report = assessor.assess_risks(
    company_data=company_financial_data,
    assessment_scope="operational"
)

print(risk_report)
```

#### 3. Generate Executive Report

```python
from financial_ai_platform import ReportGenerator

generator = ReportGenerator()

# Generate executive summary
report = generator.generate_report(
    analysis_data=financial_analysis,
    report_type="executive_summary"
)

print(report)
```

### Running the API Server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` to access the interactive API documentation.

### Example API Calls

#### Upload Document for Analysis

```bash
curl -X POST "http://localhost:8000/api/documents/analyze" \
  -F "file=@financial_document.pdf" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Get Risk Assessment

```bash
curl -X POST "http://localhost:8000/api/risk/assess" \
  -H "Content-Type: application/json" \
  -d '{
    "company_id": "123",
    "analysis_date": "2026-06-05"
  }'
```

---

## 🏗 Architecture

### System Components

```
┌─────────────────────────────────────────┐
│      Document Input Layer               │
│  (PDF, Excel, Word, etc.)              │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│    Document Processing Engine           │
│  (Parsing, Extraction, Normalization)  │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│      Multi-Agent Crew System            │
│  ┌──────────┐  ┌──────────┐            │
│  │ Analyst  │  │ Assessor │            │
│  │ Agent    │  │ Agent    │            │
│  └──────────┘  └──────────┘            │
│  ┌──────────┐  ┌──────────┐            │
│  │ Reporter │  │ Research │            │
│  │ Agent    │  │ Agent    │            │
│  └──────────┘  └──────────┘            │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│  Vector Database (FAISS)                │
│  Semantic Search & Retrieval            │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│    Report Generation & Output           │
│  (Executive Summary, Risk Report, etc.) │
└─────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
financial-ai-platform/
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── .env.example                   # Example environment variables
├── .gitignore                     # Git ignore rules
│
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # Configuration settings
│   └── routes/
│       ├── documents.py           # Document endpoints
│       ├── analysis.py            # Analysis endpoints
│       └── reports.py             # Report endpoints
│
├── agents/
│   ├── __init__.py
│   ├── analyst_agent.py           # Financial analyst agent
│   ├── assessor_agent.py          # Risk assessor agent
│   ├── reporter_agent.py          # Report generation agent
│   └── research_agent.py          # Research assistant agent
│
├── services/
│   ├── __init__.py
│   ├── document_processor.py      # Document processing logic
│   ├── vector_store.py            # FAISS vector store manager
│   ├── openai_service.py          # OpenAI API integration
│   └── analysis_engine.py         # Analysis execution engine
│
├── models/
│   ├── __init__.py
│   ├── schemas.py                 # Pydantic schemas
│   └── entities.py                # Data models
│
├── utils/
│   ├── __init__.py
│   ├── logger.py                  # Logging configuration
│   ├── validators.py              # Input validators
│   └── helpers.py                 # Utility functions
│
├── data/
│   ├── vector_store/              # FAISS vector database
│   ├── documents/                 # Uploaded documents
│   └── reports/                   # Generated reports
│
└── tests/
    ├── __init__.py
    ├── test_agents.py             # Agent tests
    ├── test_services.py           # Service tests
    └── test_api.py                # API endpoint tests
```

---

## 🔧 Advanced Configuration

### Custom Agent Configuration

Edit `agents/config.yaml`:

```yaml
analyst_agent:
  role: "Financial Analyst"
  goal: "Analyze financial documents"
  backstory: "Expert in financial analysis"
  model: "gpt-4"
  temperature: 0.7

assessor_agent:
  role: "Risk Assessor"
  goal: "Assess business risks"
  backstory: "Risk management expert"
  model: "gpt-4"
  temperature: 0.5
```

### Vector Store Configuration

Adjust FAISS settings in `services/vector_store.py`:

```python
# Vector dimension
VECTOR_DIMENSION = 1536  # OpenAI embedding dimension

# Index type
INDEX_TYPE = "IVF"  # or "HNSW", "FLAT"

# Batch size
BATCH_SIZE = 100
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_agents.py -v
```

---

## 📊 Performance Optimization

1. **Parallel Agent Execution**: Agents run in parallel for faster analysis
2. **Vector Indexing**: Use FAISS for O(1) document retrieval
3. **Caching**: Implement result caching to avoid redundant processing
4. **Batch Processing**: Process multiple documents in batches

---

## 🐛 Troubleshooting

### Issue: "OpenAI API Key not found"
**Solution**: Ensure `.env` file exists and contains `OPENAI_API_KEY`

### Issue: "FAISS index not found"
**Solution**: Initialize vector database:
```bash
python -c "from services.vector_store import VectorStore; VectorStore().initialize()"
```

### Issue: "Module not found" errors
**Solution**: Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Issue: "Out of memory"
**Solution**: Reduce batch size in configuration or process documents individually

---

## 📚 Additional Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [FAISS Documentation](https://faiss.ai/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines:
- Write clear commit messages
- Add tests for new features
- Update documentation
- Follow PEP 8 style guide

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For support and questions:

- **GitHub Issues**: [Create an issue](https://github.com/drdeveloper88/financial-ai-platform/issues)
- **Discussions**: [Start a discussion](https://github.com/drdeveloper88/financial-ai-platform/discussions)
- **Email**: drdeveloper88@example.com

---

## 🙏 Acknowledgments

- OpenAI for GPT models
- Crew AI team for the multi-agent framework
- LangChain community for LangGraph
- Facebook Research for FAISS

---

## 📈 Roadmap

- [ ] Add support for real-time data feeds
- [ ] Implement machine learning model training
- [ ] Add multi-language support
- [ ] Create web dashboard UI
- [ ] Add Kubernetes deployment templates
- [ ] Implement advanced caching strategies

---

**Last Updated**: June 5, 2026  
**Version**: 1.0.0  
**Status**: Active Development

---

<div align="center">

Made with ❤️ by [drdeveloper88](https://github.com/drdeveloper88)

[⭐ Star us on GitHub!](https://github.com/drdeveloper88/financial-ai-platform)

</div>
