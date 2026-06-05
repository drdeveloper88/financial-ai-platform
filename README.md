# Financial AI Platform 🤖💼

An agentic AI platform for financial document analysis, risk assessment, and executive reporting using **CrewAI**, **LangGraph**, **OpenAI**, and **FAISS**.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Agents & Tasks](#agents--tasks)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

The Financial AI Platform is an intelligent multi-agent system designed to analyze financial documents, assess business risks, and generate comprehensive executive reports. It leverages **CrewAI** for agent orchestration and **OpenAI GPT-4o-mini** for intelligent analysis.

### Key Capabilities:
- **Document Extraction**: Extract financial information from documents
- **Financial Analysis**: Analyze company financial health and performance
- **Risk Assessment**: Identify and evaluate financial and operational risks
- **Executive Reporting**: Generate professional executive summaries and reports
- **Vector-based Search**: Fast and intelligent document retrieval using FAISS
- **Multi-Agent Workflow**: Specialized agents working together for comprehensive analysis

---

## ✨ Features

- ✅ Multi-agent AI system powered by **CrewAI**
- ✅ 5 specialized agents (Document, Financial, Risk, Report, Extraction)
- ✅ FastAPI REST API for easy integration
- ✅ Document extraction and financial metrics analysis
- ✅ Risk assessment and recommendations
- ✅ Executive summary generation
- ✅ Vector database integration (FAISS) for semantic search
- ✅ OpenAI GPT-4o-mini integration for intelligent analysis
- ✅ LangGraph for workflow orchestration
- ✅ Environment-based configuration

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Core programming language |
| **FastAPI** | REST API framework |
| **Uvicorn** | ASGI server |
| **CrewAI** | Multi-agent orchestration |
| **LangGraph** | Workflow graph execution |
| **LangChain OpenAI** | OpenAI integration |
| **OpenAI** | GPT-4o-mini LLM |
| **FAISS** | Vector similarity search |
| **Pydantic** | Data validation |
| **Python-dotenv** | Environment management |
| **NumPy** | Numerical computing |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Git**
- **OpenAI API Key** (from [platform.openai.com](https://platform.openai.com))

### System Requirements:
- RAM: Minimum 4GB (8GB recommended)
- Storage: At least 1GB free space
- OS: Windows, macOS, or Linux

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

Create a `.env` file in the project root directory:

```bash
touch .env
```

### Step 2: Add Configuration Variables

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 3: Obtain OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Sign in with your account
3. Navigate to **API keys** section
4. Click **Create new secret key**
5. Copy the key and paste it in your `.env` file

**Note:** Keep your API key private and never commit it to version control.

---

## 📁 Project Structure

```
financial-ai-platform/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── main.py                            # FastAPI application entry point
│
├── agents/                            # AI Agent definitions
│   ├── __init__.py
│   ├── financial_agent.py             # Financial analysis agent
│   ├── risk_agent.py                  # Risk assessment agent
│   ├── report_agent.py                # Report generation agent
│   ├── document_agent.py              # Document extraction agent
│   └── [Additional agents]
│
├── tasks/                             # Task definitions for agents
│   ├── __init__.py
│   ├── analysis_task.py               # Financial analysis tasks
│   ├── risk_task.py                   # Risk assessment tasks
│   ├── report_task.py                 # Report generation tasks
│   ├── extraction_task.py             # Document extraction tasks
│   └── [Additional tasks]
│
├── api/                               # FastAPI REST API
│   ├── __init__.py
│   └── financial_api.py               # API routes and endpoints
│
├── config/                            # Configuration management
│   ├── __init__.py
│   └── settings.py                    # Settings and environment variables
│
├── workflows/                         # LangGraph workflow definitions
│   ├── [Workflow implementations]
│   └── [Orchestration logic]
│
└── .gitignore                         # Git ignore file
```

---

## 🚀 Usage

### Running the FastAPI Server

```bash
python main.py
```

Or with Uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

Interactive API docs: `http://localhost:8000/docs`

### Basic API Usage

#### Analyze Financial Document

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "document_text": "Your financial document content here..."
  }'
```

**Response:**
```json
{
  "message": "Workflow implementation placeholder",
  "input": "Your financial document content here..."
}
```

### Python Usage Example

```python
from agents.financial_agent import get_financial_agent
from agents.risk_agent import get_risk_agent
from agents.report_agent import get_report_agent
from tasks.analysis_task import build_analysis_task
from tasks.risk_task import build_risk_task
from tasks.report_task import build_report_task
from crewai import Crew

# Create agents
financial_agent = get_financial_agent()
risk_agent = get_risk_agent()
report_agent = get_report_agent()

# Create tasks
analysis_task = build_analysis_task(financial_agent, "company_financial_data")
risk_task = build_risk_task(risk_agent, "company_financial_data")
report_task = build_report_task(report_agent, "analysis_results")

# Create crew
crew = Crew(agents=[financial_agent, risk_agent, report_agent], tasks=[analysis_task, risk_task, report_task])

# Execute workflow
result = crew.kickoff()
print(result)
```

---

## 🤖 Agents & Tasks

### Available Agents

#### 1. **Financial Analyst Agent**
- **File**: `agents/financial_agent.py`
- **Role**: Analyze company performance
- **Goal**: Provide detailed financial analysis
- **Backstory**: Experienced banking analyst

#### 2. **Risk Assessment Agent**
- **File**: `agents/risk_agent.py`
- **Role**: Risk Assessment Agent
- **Goal**: Identify risks in financial data
- **Backstory**: Risk specialist

#### 3. **Executive Report Agent**
- **File**: `agents/report_agent.py`
- **Role**: Executive Report Generator
- **Goal**: Create executive summaries
- **Backstory**: Reporting expert

#### 4. **Document Extraction Agent**
- **File**: `agents/document_agent.py`
- **Role**: Document Extraction Agent
- **Goal**: Extract financial information from documents
- **Backstory**: Expert in annual reports

### Available Tasks

#### 1. **Financial Analysis Task**
```python
build_analysis_task(agent, financial_data)
# Description: "Analyze financial health: {data}"
```

#### 2. **Risk Assessment Task**
```python
build_risk_task(agent, financial_data)
# Description: "Assess risks: {data}"
```

#### 3. **Report Generation Task**
```python
build_report_task(agent, analysis_results)
# Description: "Generate executive report: {data}"
```

#### 4. **Document Extraction Task**
```python
build_extraction_task(agent, document_text)
# Description: "Extract financial metrics from: {text}"
```

---

## 📡 API Endpoints

### POST `/analyze`
Analyze financial documents and generate insights.

**Request:**
```json
{
  "document_text": "string"
}
```

**Response:**
```json
{
  "message": "string",
  "input": "string"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"document_text": "Q3 2025 Financial Report..."}'
```

---

## 🔧 Configuration Details

### Model Settings

The platform uses **GPT-4o-mini** by default. To change the model:

**File**: `config/settings.py`

```python
MODEL_NAME = "gpt-4o-mini"  # Change this to your preferred model
```

Available models:
- `gpt-4o` - Faster and more advanced
- `gpt-4o-mini` - Lightweight and cost-effective (default)
- `gpt-4-turbo` - Previous generation

### Environment Variables

Add these to your `.env` file:

```env
# Required
OPENAI_API_KEY=your_api_key_here

# Optional
# LOG_LEVEL=INFO
# DEBUG=False
```

---

## 📊 Workflow Overview

```
┌─────────────────────────┐
│   Financial Document    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Document Extraction    │
│      Agent Task         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Financial Analysis    │
│      Agent Task         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Risk Assessment       │
│      Agent Task         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Executive Report      │
│      Agent Task         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Final Report & Data   │
└─────────────────────────┘
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'crewai'"
**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "OPENAI_API_KEY not found"
**Solution**: 
1. Create `.env` file in project root
2. Add your OpenAI API key: `OPENAI_API_KEY=your_key_here`

### Issue: "Connection error to OpenAI API"
**Solution**:
1. Verify your API key is valid
2. Check internet connection
3. Ensure you have API credits available

### Issue: "Agents not responding"
**Solution**:
1. Check if OpenAI API is operational
2. Verify your model name in `config/settings.py`
3. Check error logs for details

---

## 🚀 Next Steps

1. **Test the API**: Visit `http://localhost:8000/docs` to test endpoints
2. **Customize Agents**: Modify agent roles and backstories in `agents/` folder
3. **Add New Tasks**: Create new task definitions in `tasks/` folder
4. **Extend Workflows**: Build complex workflows in `workflows/` folder
5. **Deploy**: Deploy to cloud platforms like Heroku, AWS, or Azure

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
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines:
- Write clear commit messages
- Follow Python PEP 8 style guide
- Add comments for complex logic
- Test your changes before submitting

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

For support and questions:

- **GitHub Issues**: [Create an issue](https://github.com/drdeveloper88/financial-ai-platform/issues)
- **GitHub Discussions**: [Start a discussion](https://github.com/drdeveloper88/financial-ai-platform/discussions)
- **Email**: drdeveloper88@example.com

---

## 📈 Project Status

- ✅ Basic project structure
- ✅ Agent framework setup
- ✅ FastAPI integration
- 🔄 Full workflow implementation (In Progress)
- ⏳ FAISS vector search (Planned)
- ⏳ Advanced analytics (Planned)

---

## 🙏 Acknowledgments

- OpenAI for GPT models
- CrewAI team for the multi-agent framework
- LangChain community for LangGraph
- Facebook Research for FAISS

---

<div align="center">

**Made with ❤️ by [drdeveloper88](https://github.com/drdeveloper88)**

[⭐ Star us on GitHub!](https://github.com/drdeveloper88/financial-ai-platform)

</div>

---

**Last Updated**: June 5, 2026 | **Version**: 1.0.0 | **Status**: Active Development
