# Multi-Agent Leave Management System

A comprehensive employee leave management system built with LangGraph, featuring multiple AI agents that work together to handle leave requests, policy queries, and employee data management.

## 🎯 Project Overview

This project implements a sophisticated multi-agent system for employee leave management using LangGraph and LangChain. The system consists of specialized AI agents that collaborate to provide intelligent leave management services, including policy interpretation, leave request processing, and employee data retrieval.

## 📁 Project Structure

```
multi_agent_langgraph/
├── documents/
│   └── Employee_Leave_Policy.pdf          # Company leave policy document
├── src/
│   ├── agents/                           # Jupyter notebooks for different agents
│   │   ├── 1_fetch_data_agent.ipynb      # Basic data fetching agent
│   │   ├── 2_fetch_data_agent_adv.ipynb  # Advanced data fetching agent
│   │   ├── 3_read_policy_agentic.ipynb   # Policy reading and interpretation agent
│   │   ├── 4_email_agentic_w_graph.ipynb # Email processing with LangGraph
│   │   ├── 5_email_agentic.ipynb         # Email processing agent
│   │   └── 6_leave_mgnt_multi_agent.ipynb # Main multi-agent system
│   └── flask_app/                        # Web application
│       ├── app_auth.py                   # Authentication module
│       └── read_data_app.py              # Main Flask application
├── requirement-aiagent.txt               # Dependencies for AI agents
├── requirement-webapp.txt                # Dependencies for web application
└── README.md                             # This file
```

## 🤖 Agent Architecture

The system consists of several specialized agents:

### 1. Data Fetching Agents
- **Basic Data Agent** (`1_fetch_data_agent.ipynb`): Simple employee data retrieval
- **Advanced Data Agent** (`2_fetch_data_agent_adv.ipynb`): Enhanced data fetching with additional features

### 2. Policy Interpretation Agent
- **Policy Reader** (`3_read_policy_agentic.ipynb`): Analyzes and interprets company leave policies using document embeddings and vector search

### 3. Email Processing Agents
- **Email Agent with Graph** (`4_email_agentic_w_graph.ipynb`): Processes leave request emails using LangGraph workflows
- **Email Agent** (`5_email_agentic.ipynb`): Standalone email processing capabilities

### 4. Multi-Agent System
- **Main System** (`6_leave_mgnt_multi_agent.ipynb`): Orchestrates all agents using LangGraph for comprehensive leave management

## 🌐 Web Application

The Flask web application provides a user-friendly interface for:
- Employee authentication
- Leave balance queries
- Employee data retrieval
- Integration with the AI agent system

### Key Features:
- RESTful API endpoints
- Employee authentication system
- JSON-based data exchange
- Session management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- OpenAI API key
- Required Python packages (see requirements files)

### 1. Install AI Agent Dependencies
```bash
pip install -r requirement-aiagent.txt
```

### 2. Install Web Application Dependencies
```bash
pip install -r requirement-webapp.txt
```

### 3. Environment Setup
Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 📋 Dependencies

### AI Agents (`requirement-aiagent.txt`)
- `load_dotenv` - Environment variable management
- `requests` - HTTP library
- `langchain-openai` - OpenAI integration for LangChain
- `pydantic` - Data validation
- `openai` - OpenAI Python client
- `langsmith` - LangChain observability
- `langgraph` - Multi-agent orchestration
- `langchain-core` - Core LangChain functionality

### Web Application (`requirement-webapp.txt`)
- `pyrebase4` - Firebase integration
- `Flask` - Web framework

## 🎮 Usage

### Running the Multi-Agent System

1. **Navigate to the agents directory:**
   ```bash
   cd src/agents
   ```

2. **Open the main multi-agent notebook:**
   ```bash
   jupyter notebook 6_leave_mgnt_multi_agent.ipynb
   ```

3. **Follow the notebook cells to:**
   - Load and process the leave policy document
   - Set up vector embeddings
   - Initialize the multi-agent system
   - Test the system with sample queries

### Running the Web Application

1. **Navigate to the Flask app directory:**
   ```bash
   cd src/flask_app
   ```

2. **Run the Flask application:**
   ```bash
   python read_data_app.py
   ```

3. **Access the application:**
   - Open your browser and go to `http://localhost:5000`
   - Use the API endpoints for employee data retrieval

## 🔧 API Endpoints

### Web Application Endpoints

- `GET /` - Home page
- `POST /find_details` - Get employee details (requires username and password)

### Sample API Usage
```bash
curl -X POST http://localhost:5000/find_details \
  -F "username=priya@gmail.com" \
  -F "password=password123"
```

## 📊 Sample Employee Data

The system includes sample employee data with the following structure:
- Employee ID
- First and Last Name
- Username (email)
- Basic Salary
- Earn Leaves Balance
- Sick Leaves Balance

## 🔍 Key Features

1. **Intelligent Policy Interpretation**: Uses vector embeddings to search and interpret company leave policies
2. **Multi-Agent Collaboration**: Different agents specialize in specific tasks and work together
3. **Document Processing**: Handles PDF documents and extracts relevant information
4. **Email Processing**: Can process leave request emails and generate responses
5. **Web Interface**: User-friendly web application for data access
6. **Authentication**: Secure employee authentication system

## 🛠️ Technical Implementation

- **Vector Database**: ChromaDB for document embeddings and similarity search
- **LLM Integration**: OpenAI GPT models for natural language processing
- **Agent Orchestration**: LangGraph for managing multi-agent workflows
- **Document Processing**: LangChain document loaders and text splitters
- **Web Framework**: Flask for the web application
- **Authentication**: Custom authentication system with session management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational and demonstration purposes.

## 🆘 Support

For issues and questions, please refer to the individual notebook files for detailed implementation notes and examples.
