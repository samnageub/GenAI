# 🤖 GenAI Explorer
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜_LangChain-AI-green?style=for-the-badge)
![Ollama](https://img.shields.io/badge/Ollama-Local_AI-orange?style=for-the-badge)

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Components](#components)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Security](#security)

## Overview
A comprehensive GenAI toolkit featuring local DeepSeek model implementation, document processing (RAG), and integration with various services including Airbnb booking and OpenAI API.

## System Architecture

### Complete System Flow
```mermaid
graph TD
    subgraph "Frontend Interfaces"
        A1[Streamlit UI - Main Chat]
        A2[Streamlit UI - RAG]
        A3[Gradio UI - Airbnb]
    end
    
    subgraph "AI Processing Layer"
        B1[DeepSeek Local]
        B2[OpenAI API]
        B3[LangChain]
    end
    
    subgraph "Document Processing"
        C1[PDF Loader]
        C2[Text Splitter]
        C3[Vector Store]
    end
    
    subgraph "External Services"
        D1[MCP Server]
        D2[Airbnb API]
        D3[OpenAI Services]
    end
    
    A1 --> B1
    A2 --> C1
    A3 --> D1
    
    C1 --> C2
    C2 --> C3
    C3 --> B3
    
    B3 --> B1
    B3 --> B2
    
    D1 --> D2
    B2 --> D3
```

### RAG Implementation Flow
```mermaid
sequenceDiagram
    participant User
    participant UI as Streamlit UI
    participant PDF as PDF Processor
    participant VS as Vector Store
    participant AI as DeepSeek AI

    User->>UI: Upload PDF
    UI->>PDF: Process Document
    PDF->>VS: Store Vectors
    User->>UI: Ask Question
    UI->>VS: Search Similar Content
    VS->>AI: Provide Context
    AI->>UI: Generate Response
    UI->>User: Display Answer
```

## Features
- 🤖 Local DeepSeek model integration (1.5b and 3b variants)
- 📚 RAG implementation with AI Health coach assistant Agent for PDF processing to analyze images and and documents and provide recommendation 
- 🏠 Airbnb booking assistant with MCP server
- 🔄 OpenAI API integration
- 💅 Custom-styled UI interfaces
- 📊 Vector store for document retrieval

## Components

### 1. Main Chat Application (`app.py`)
```python
# Key configurations
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)
```

### 2. RAG Implementation (`rag_deep.py`)
```python
# Core components
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")
```

### 3. AI Health Coach Agent RAG Implementation (`Ai_recipe_assistant.py`)
```python
# Core components
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")
```

### 4. Airbnb Search (`airbnb_search.py`)
```python
agent = Agent(
    instructions="""You help book apartments on Airbnb.""",
    llm="gpt-4o-mini",
    tools=MCP("npx -y @openbnb/mcp-server-airbnb")
)
```

## Installation

```bash
# Clone repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt

# Required packages
streamlit
langchain_core
langchain_community
langchain_ollama
pdfplumber
praisonaiagents 
mcp
openai
gradio
requests
```

## Usage

1. **Start Main Chat Interface**
```bash
streamlit run app.py
```

2. **Launch Document Assistant**
```bash
streamlit run rag_deep.py
```

3. **Launch AI Health Coach Agent Assistant**
```bash
streamlit run ai_recipe_assistant.py
```

4. **Start Airbnb Search Agent Assistant**
```bash
python airbnb_search.py
```

## Configuration

### DeepSeek Model Settings
```python
# Available models
models = ["deepseek-r1:1.5b", "deepseek-r1:3b"]

# RAG Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

## Security
- 🔒 Secure API key management
- 🏢 Local model execution
- 🔐 No data persistence
- 📄 Safe document handling

---
📝 **Note:** Ensure all API keys and configurations are properly set before running the applications.

This README now includes:
- Detailed system architecture diagrams
- Component interaction flows
- Code snippets from actual implementation
- Clear installation and usage instructions
- Security considerations

