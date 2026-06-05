# Financial AI Platform 🤖💼

An advanced agentic AI platform for financial document analysis, risk assessment, and executive reporting using **CrewAI**, **LangGraph**, **OpenAI**, and **FAISS** with real-time processing capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [API Endpoints](#api-endpoints)
- [Agents & Tasks](#agents--tasks)
- [Workflows](#workflows)
- [RAG System](#rag-system)
- [Services](#services)
- [Configuration Details](#configuration-details)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

The Financial AI Platform is an intelligent multi-agent system designed to analyze financial documents, assess business risks, and generate comprehensive executive reports in real-time. It leverages **CrewAI** for agent orchestration, **LangGraph** for workflow management, and **FAISS** for intelligent document retrieval.

### Key Capabilities:
- **Document Extraction**: Intelligent extraction of financial information from documents
- **Financial Analysis**: Deep analysis of company financial health and performance metrics
- **Risk Assessment**: Comprehensive identification and evaluation of financial and operational risks
- **Executive Reporting**: Professional executive summaries and detailed reports generation
- **Vector-based Search**: Fast and intelligent document retrieval using FAISS embeddings
- **Multi-Agent Workflow**: Specialized agents working together for comprehensive analysis
- **Real-time Processing**: Live data processing and analysis with immediate results
- **RAG Integration**: Retrieval-Augmented Generation for context-aware insights

---

## ✨ Features

- ✅ **Multi-Agent Architecture**: 4 specialized agents powered by **CrewAI**
- ✅ **Real-time Processing**: Live financial data analysis and monitoring
- ✅ **FastAPI REST API**: Scalable REST API for easy integration
- ✅ **Document Extraction**: Extract financial metrics from unstructured documents
- ✅ **Advanced Analytics**: Financial health scoring and performance metrics
- ✅ **Risk Assessment**: Identify and evaluate financial and operational risks
- ✅ **Executive Reporting**: Automated professional report generation
- ✅ **RAG System**: Retrieval-Augmented Generation with vector embeddings
- ✅ **Vector Database**: FAISS integration for semantic search and similarity matching
- ✅ **LangGraph Workflows**: Sophisticated workflow orchestration and state management
- ✅ **OpenAI Integration**: GPT-4o-mini for intelligent analysis and reasoning
- ✅ **Environment Configuration**: Flexible configuration management
- ✅ **Modular Services**: Decoupled service architecture for scalability
- ✅ **Production Ready**: Error handling, logging, and monitoring

---

## 🛠 Tech Stack

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Core programming language | 3.9+ |
| **FastAPI** | REST API framework | Latest |
| **Uvicorn** | ASGI server | Latest |
| **CrewAI** | Multi-agent orchestration | Latest |
| **LangGraph** | Workflow graph execution | Latest |
| **LangChain** | LLM framework | Latest |
| **OpenAI** | GPT-4o-mini LLM | Latest |
| **FAISS** | Vector similarity search | Latest |
| **Pydantic** | Data validation | v2+ |
| **Python-dotenv** | Environment management | Latest |
| **NumPy** | Numerical computing | Latest |

---

## 📁 Project Structure

```
financial-ai-platform/

├── app/                                   # Application module
│
├── agents/                                # AI Agent definitions
│   ├── __init__.py
│   ├── document_agent.py                  # Document extraction & processing agent
│   ├── financial_agent.py                 # Financial analysis agent
│   ├── risk_agent.py                      # Risk assessment agent
│   └── report_agent.py                    # Executive report generation agent
│
├── tasks/                                 # Task definitions for agents
│   ├── __init__.py
│   ├── extraction_task.py                 # Document extraction tasks
│   ├── analysis_task.py                   # Financial analysis tasks
│   ├── risk_task.py                       # Risk assessment tasks
│   └── report_task.py                     # Report generation tasks
│
├── workflows/                             # LangGraph workflow orchestration
│   ├── __init__.py
│   ├── state.py                           # Workflow state management
│   └── financial_workflow.py               # Main financial workflow definition
│
├── rag/                                   # Retrieval-Augmented Generation system
│   ├── __init__.py
│   ├── embeddings.py                      # Embedding generation & management
│   ├── vector_store.py                    # FAISS vector store operations
│   └── retriever.py                       # Document retrieval logic
│
├── services/                              # Business logic services
│   ├── __init__.py
│   └── financial_service.py               # Core financial service logic
│
├── api/                                   # FastAPI REST endpoints
│   ├── __init__.py
│   └── financial_api.py                   # API routes and endpoint handlers
│
├── config/                                # Configuration management
│   ├── __init__.py
│   └── settings.py                        # Settings and environment variables
│
├── main.py                                # FastAPI application entry point
├── .env                                   # Environment variables (create manually)
├── requirements.txt                       # Python dependencies
├── README.md                              # This file
└── .gitignore                             # Git ignore file
```

### Module Descriptions

#### **agents/**
Contains all AI agent definitions. Each agent has specific roles and responsibilities:
- **Document Agent**: Processes and extracts information from financial documents
- **Financial Agent**: Analyzes financial metrics and company performance
- **Risk Agent**: Identifies and assesses financial and operational risks
- **Report Agent**: Generates professional executive reports

#### **tasks/**
Defines specific tasks for each agent to execute:
- **Extraction Task**: Extract financial data from documents
- **Analysis Task**: Analyze financial health and metrics
- **Risk Task**: Assess and evaluate risks
- **Report Task**: Generate comprehensive reports

#### **workflows/**
LangGraph-based workflow orchestration:
- **state.py**: Manages workflow state throughout execution
- **financial_workflow.py**: Defines the complete financial analysis workflow

#### **rag/**
Retrieval-Augmented Generation system for intelligent search:
- **embeddings.py**: Generates and manages text embeddings
- **vector_store.py**: FAISS vector database operations
- **retriever.py**: Retrieves relevant documents for context

#### **services/**
Core business logic services:
- **financial_service.py**: Main service handling financial operations

#### **api/**
FastAPI REST API:
- **financial_api.py**: API routes and endpoint handlers

#### **config/**
Configuration management:
- **settings.py**: Application settings and environment variables

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Git**
- **OpenAI API Key** (from [platform.openai.com](https://platform.openai.com))

### System Requirements:
- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: At least 2GB free space
- **OS**: Windows, macOS, or Linux
- **Internet**: Required for OpenAI API access

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/drdeveloper88/financial-ai-platform.git
cd financial-ai-platform
```

### Step 2: Create a Virtual Environment (Recommended)

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
python -c "import fastapi; import crewai; import faiss; print('✅ Installation successful!')"
```

---

## ⚙️ Configuration

### Step 1: Create Environment File

Create a `.env` file in the project root:

```bash
touch .env
```

### Step 2: Add Configuration Variables

Add your OpenAI API key and other settings:

```env
# Required
OPENAI_API_KEY=sk-your_openai_api_key_here

# Optional Settings
API_HOST=0.0.0.0
API_PORT=8000
LOG_LEVEL=INFO
DEBUG=False
MODEL_NAME=gpt-4o-mini

# RAG Settings
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_STORE_PATH=./data/vectors
```

### Step 3: Obtain OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Sign in with your account
3. Navigate to **API keys** → **Create new secret key**
4. Copy the key and paste it in your `.env` file

**⚠️ Security Note**: Never commit `.env` to version control!

---

## 🚀 Quick Start

### Running the FastAPI Server

```bash
python main.py
```

Or with Uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: `http://localhost:8000`
- **API Docs**: `http://localhost:8000/docs` (Interactive Swagger UI)
- **ReDoc**: `http://localhost:8000/redoc`

---

## 💡 Usage Examples

### Example 1: Analyze Financial Document via API

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "document_text": "Q3 2025 Financial Report: Revenue increased by 15% YoY to $2.5B..."
  }'
```

**Response:**
```json
{
  "status": "success",
  "analysis": {
    "financial_metrics": {
      "revenue": "$2.5B",
      "growth_rate": "15%"
    },
    "risks": [
      {
        "risk_type": "market",
        "severity": "medium",
        "description": "Market volatility affecting growth"
      }
    ],
    "recommendations": [
      "Diversify revenue streams",
      "Strengthen risk management"
    ]
  },
  "report": "Executive summary with detailed analysis..."
}
```

### Example 2: Python Integration

```python
from agents.financial_agent import get_financial_agent
from agents.risk_agent import get_risk_agent
from agents.report_agent import get_report_agent
from tasks.analysis_task import build_analysis_task
from tasks.risk_task import build_risk_task
from tasks.report_task import build_report_task
from crewai import Crew

# Initialize agents
financial_agent = get_financial_agent()
risk_agent = get_risk_agent()
report_agent = get_report_agent()

# Define tasks
analysis_task = build_analysis_task(financial_agent, financial_data)
risk_task = build_risk_task(risk_agent, financial_data)
report_task = build_report_task(report_agent, analysis_results)

# Create and execute crew
crew = Crew(
    agents=[financial_agent, risk_agent, report_agent],
    tasks=[analysis_task, risk_task, report_task]
)

result = crew.kickoff()
print(result)
```

### Example 3: RAG-based Document Search

```python
from rag.retriever import DocumentRetriever

# Initialize retriever
retriever = DocumentRetriever()

# Add documents to knowledge base
retriever.add_document("Financial Report Q3 2025", financial_text)

# Search for relevant documents
relevant_docs = retriever.retrieve("revenue growth trends", top_k=5)

for doc in relevant_docs:
    print(f"Document: {doc['title']}")
    print(f"Similarity Score: {doc['score']}")
    print(f"Content: {doc['content'][:200]}...")
```

---

## 📡 API Endpoints

### Core Endpoints

#### 1. **POST `/api/analyze`**
Analyze financial documents and generate comprehensive insights.

**Request:**
```json
{
  "document_text": "string"
}
```

**Response:**
```json
{
  "status": "success",
  "analysis": { },
  "risks": [ ],
  "report": "string"
}
```

#### 2. **POST `/api/extract`**
Extract financial metrics from unstructured documents.

**Request:**
```json
{
  "document_text": "string"
}
```

**Response:**
```json
{
  "extracted_metrics": { },
  "confidence_scores": { }
}
```

#### 3. **POST `/api/risk-assessment`**
Perform comprehensive risk assessment.

**Request:**
```json
{
  "financial_data": "string"
}
```

**Response:**
```json
{
  "risks": [ ],
  "severity_levels": { },
  "recommendations": [ ]
}
```

#### 4. **POST `/api/generate-report`**
Generate executive report from analysis results.

**Request:**
```json
{
  "analysis_results": "string"
}
```

**Response:**
```json
{
  "report": "string",
  "summary": "string",
  "recommendations": [ ]
}
```

#### 5. **POST `/api/search`**
Search documents using RAG system.

**Request:**
```json
{
  "query": "string",
  "top_k": 5
}
```

**Response:**
```json
{
  "results": [
    {
      "title": "string",
      "content": "string",
      "similarity_score": 0.95
    }
  ]
}
```

#### 6. **GET `/health`**
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-06-05T10:30:00Z"
}
```

---

## 🤖 Agents & Tasks

### Agent Architecture

#### **1. Document Agent** 📄
- **File**: `agents/document_agent.py`
- **Role**: Document Processing Specialist
- **Goal**: Extract and structure financial information from documents
- **Expertise**: Annual reports, financial statements, regulatory filings
- **Output**: Structured financial data

#### **2. Financial Agent** 💰
- **File**: `agents/financial_agent.py`
- **Role**: Financial Analyst
- **Goal**: Analyze company financial performance and health
- **Expertise**: Financial metrics, ratios, trend analysis
- **Output**: Financial analysis and insights

#### **3. Risk Agent** ⚠️
- **File**: `agents/risk_agent.py`
- **Role**: Risk Assessment Specialist
- **Goal**: Identify and evaluate financial and operational risks
- **Expertise**: Risk modeling, scenario analysis, mitigation strategies
- **Output**: Risk assessment and recommendations

#### **4. Report Agent** 📊
- **File**: `agents/report_agent.py`
- **Role**: Executive Report Generator
- **Goal**: Create professional executive summaries and reports
- **Expertise**: Report writing, summarization, presentation
- **Output**: Executive reports and summaries

### Task Definitions

#### **Extraction Task**
```python
build_extraction_task(document_agent, document_text)
# Extracts financial metrics: revenue, expenses, assets, liabilities, ratios
```

#### **Analysis Task**
```python
build_analysis_task(financial_agent, financial_data)
# Analyzes: financial health, performance metrics, trends, benchmarking
```

#### **Risk Task**
```python
build_risk_task(risk_agent, financial_data)
# Assesses: market risks, operational risks, financial risks, credit risks
```

#### **Report Task**
```python
build_report_task(report_agent, analysis_results)
# Generates: executive summary, detailed analysis, recommendations
```

---

## 🔄 Workflows

### LangGraph Workflow System

The platform uses **LangGraph** for sophisticated workflow orchestration:

#### **State Management** (`workflows/state.py`)
Manages the workflow state throughout execution:
```python
class FinancialWorkflowState:
    document_text: str
    extracted_data: dict
    analysis_results: dict
    risks: list
    report: str
    recommendations: list
```

#### **Financial Workflow** (`workflows/financial_workflow.py`)
Complete workflow pipeline:

```
Input Document
       ↓
┌─────────────────────────────┐
│  Document Extraction        │
│  (Analyze & Extract Data)   │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Financial Analysis         │
│  (Analyze Metrics & Health) │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Risk Assessment            │
│  (Identify & Evaluate Risk) │
└──────────┬──────────────────┘
           ↓
┌─────────────────────────────┐
│  Report Generation          │
│  (Create Executive Report)  │
└──────────┬──────────────────┘
           ↓
    Final Report & Insights
```

---

## 🧠 RAG System

### Retrieval-Augmented Generation

The RAG system enables intelligent document retrieval and context-aware analysis:

#### **Embeddings** (`rag/embeddings.py`)
- Generate text embeddings using OpenAI
- Store embeddings in vector format
- Support for batch processing

#### **Vector Store** (`rag/vector_store.py`)
- FAISS-based vector storage
- Efficient similarity search
- Persistent storage support

#### **Retriever** (`rag/retriever.py`)
- Retrieve relevant documents for queries
- Similarity-based ranking
- Context injection for analysis

### Usage Example

```python
from rag.retriever import DocumentRetriever

retriever = DocumentRetriever()

# Add documents
retriever.add_document("2025 Annual Report", document_content)

# Retrieve relevant documents
results = retriever.retrieve("revenue analysis", top_k=5)

# Results include similarity scores and content
for result in results:
    print(f"Score: {result['score']:.2%}")
    print(f"Content: {result['content']}")
```

---

## 🔧 Services

### Financial Service (`services/financial_service.py`)

Core business logic for financial operations:

```python
class FinancialService:
    def extract_metrics(document_text: str) -> dict
    def analyze_financial_health(metrics: dict) -> dict
    def assess_risks(financial_data: dict) -> list
    def generate_report(analysis: dict) -> str
    def calculate_ratios(financial_data: dict) -> dict
```

---

## ⚙️ Configuration Details

### Model Configuration

**File**: `config/settings.py`

```python
# Model Settings
MODEL_NAME = "gpt-4o-mini"  # Default model
TEMPERATURE = 0.7           # Creativity level
MAX_TOKENS = 4096           # Maximum response length

# API Settings
API_HOST = "0.0.0.0"
API_PORT = 8000
API_TIMEOUT = 300           # 5 minutes

# RAG Settings
EMBEDDING_MODEL = "text-embedding-3-small"
VECTOR_STORE_PATH = "./data/vectors"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/financial-ai.log"
```

### Available Models

| Model | Speed | Cost | Quality |
|-------|-------|------|---------|
| `gpt-4o` | Fast | Higher | Highest |
| `gpt-4o-mini` | Very Fast | Low | High |
| `gpt-4-turbo` | Medium | High | Very High |

### Environment Variables

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-...
OPENAI_ORG_ID=org-...

# Application Settings
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False
LOG_LEVEL=INFO

# Model Configuration
MODEL_NAME=gpt-4o-mini
TEMPERATURE=0.7
MAX_TOKENS=4096

# RAG Configuration
EMBEDDING_MODEL=text-embedding-3-small
VECTOR_STORE_PATH=./data/vectors

# Database
VECTOR_DB_TYPE=faiss
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'crewai'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "OPENAI_API_KEY not found"
**Solution**:
1. Create `.env` file in project root
2. Add: `OPENAI_API_KEY=sk-your_key_here`
3. Restart the application

### Issue: "Connection error to OpenAI API"
**Solution**:
1. Verify API key is valid and has active credits
2. Check internet connection
3. Check OpenAI service status
4. Verify firewall/proxy settings

### Issue: "FAISS index not found"
**Solution**:
1. Initialize vector store: `retriever.initialize()`
2. Add documents first
3. Check `VECTOR_STORE_PATH` setting

### Issue: "Agent response timeout"
**Solution**:
1. Increase `MAX_TOKENS` in config
2. Increase timeout in settings
3. Check API rate limits
4. Reduce document size

### Issue: "Out of memory errors"
**Solution**:
1. Reduce `CHUNK_SIZE` in RAG config
2. Process documents in batches
3. Increase system RAM
4. Use smaller embedding model

---

## 📈 Performance Optimization

### Tips for Better Performance

1. **Batch Processing**: Process multiple documents together
2. **Caching**: Cache embeddings for repeated queries
3. **Indexing**: Pre-index documents for faster retrieval
4. **Model Selection**: Use gpt-4o-mini for speed, gpt-4o for accuracy
5. **Vector Store**: Regularly optimize FAISS indices

### Monitoring

Monitor key metrics:
- API response time
- Token usage
- Vector store query time
- Agent execution time

---

## 🚀 Next Steps

1. **Test the API**: Visit `http://localhost:8000/docs`
2. **Customize Agents**: Modify agent roles in `agents/` folder
3. **Add Tasks**: Create new tasks in `tasks/` folder
4. **Build Workflows**: Create workflows in `workflows/` folder
5. **Integrate RAG**: Add documents to vector store
6. **Deploy**: Deploy to cloud (AWS, Azure, GCP, Heroku)
7. **Monitor**: Set up logging and monitoring
8. **Scale**: Implement caching and optimization

---

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [CrewAI Documentation](https://docs.crewai.com)
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [FAISS Documentation](https://faiss.ai/)

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Contributing Guidelines:
- Follow PEP 8 style guide
- Write clear, descriptive commit messages
- Add comments for complex logic
- Test changes before submitting
- Update README if needed

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For support and questions:

- **GitHub Issues**: [Create an issue](https://github.com/drdeveloper88/financial-ai-platform/issues)
- **GitHub Discussions**: [Start a discussion](https://github.com/drdeveloper88/financial-ai-platform/discussions)
- **Email**: drdeveloper88@example.com

---

## 📈 Project Status

- ✅ Project structure setup
- ✅ Agent framework implementation
- ✅ FastAPI integration
- ✅ RAG system integration
- ✅ LangGraph workflows
- 🔄 Advanced analytics (In Progress)
- ⏳ Real-time monitoring (Planned)
- ⏳ Cloud deployment templates (Planned)

---

## 🙏 Acknowledgments

- **OpenAI** for GPT models
- **CrewAI** for multi-agent framework
- **LangChain** for LLM tooling
- **Facebook Research** for FAISS
- **Pydantic** for data validation

---

<div align="center">

**Made with ❤️ by [drdeveloper88](https://github.com/drdeveloper88)**

[⭐ Star us on GitHub!](https://github.com/drdeveloper88/financial-ai-platform)

</div>

---

**Last Updated**: June 5, 2026 | **Version**: 2.0.0 | **Status**: Active Development
