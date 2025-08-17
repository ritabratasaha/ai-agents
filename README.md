# AI Agents for Employee Leave Management

A collection of AI-powered solutions for employee leave management, featuring two different implementations using modern AI frameworks and tools.

## 🎯 Project Overview

This repository contains two distinct approaches to building intelligent leave management systems:

1. **OpenAI SDK Implementation** - A simple, direct approach using OpenAI's agent framework
2. **Multi-Agent LangGraph System** - A sophisticated multi-agent orchestration using LangGraph and LangChain

## 📁 Project Structure

```
ai-agents/
├── leave_management_openai_sdk/          # OpenAI SDK implementation
│   ├── employee-leave-assist-agent.py    # Main agent implementation
│   ├── requirements.txt                  # Dependencies
│   └── Employee Leave Policy Document.pdf # Policy document
├── multi_agent_langgraph/               # LangGraph multi-agent system
│   ├── src/
│   │   ├── agents/                      # Jupyter notebooks for different agents
│   │   └── flask_app/                   # Web application
│   ├── documents/                       # Policy documents
│   ├── requirement-aiagent.txt          # AI agent dependencies
│   ├── requirement-webapp.txt           # Web app dependencies
│   └── README.md                        # Detailed documentation
└── README.md                            # This file
```

## 🚀 Quick Start

### Option 1: OpenAI SDK Implementation (Simple)

```bash
cd leave_management_openai_sdk
pip install -r requirements.txt
python employee-leave-assist-agent.py
```

**Features:**
- Direct OpenAI agent integration
- Simple triage system for routing queries
- Leave balance and policy search capabilities
- Minimal setup required

### Option 2: Multi-Agent LangGraph System (Advanced)

```bash
cd multi_agent_langgraph
pip install -r requirement-aiagent.txt
pip install -r requirement-webapp.txt
```

**Features:**
- Multi-agent orchestration with LangGraph
- Vector database for policy search
- Web application with authentication
- Email processing capabilities
- Document embedding and similarity search

## 🔧 Key Differences

| Feature | OpenAI SDK | Multi-Agent LangGraph |
|---------|------------|----------------------|
| **Complexity** | Simple | Advanced |
| **Setup** | Minimal | Comprehensive |
| **Agents** | Single triage agent | Multiple specialized agents |
| **Storage** | In-memory | Vector database (ChromaDB) |
| **Interface** | Command line | Web application |
| **Document Processing** | Basic file search | Advanced embeddings |
| **Scalability** | Limited | High |

## 🎮 Use Cases

### Choose OpenAI SDK if you want:
- Quick prototype or proof of concept
- Simple leave balance queries
- Basic policy search
- Minimal infrastructure requirements

### Choose Multi-Agent LangGraph if you want:
- Production-ready system
- Complex workflow orchestration
- Advanced document processing
- Web-based user interface
- Email automation
- Scalable architecture

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- For LangGraph: Additional dependencies (see individual READMEs)

## 🔑 Environment Setup

Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 📚 Documentation

- **Multi-Agent System**: See `multi_agent_langgraph/README.md` for detailed documentation
- **OpenAI SDK**: Check `leave_management_openai_sdk/employee-leave-assist-agent.py` for implementation details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational and demonstration purposes.

## 🆘 Support

For detailed implementation help, refer to the individual project READMEs and source code.
