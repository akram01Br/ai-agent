# 🧠 AI Agent - Multi-Agent Article Generator

An intelligent AI system that generates, researches, improves, and structures high-quality articles using multiple AI agents.

---

## 🚀 Features

- 🔍 Web search integration (DuckDuckGo API)
- 🤖 AI Writing agent (LLM-based)
- ✍️ Review & improvement agent
- 🧠 Memory system (stores generated content)
- 🌐 Flask web interface
- 📄 PDF export functionality

---

## ⚙️ How it works

1. User enters a topic
2. System searches for context
3. Research agent extracts key information
4. Writer agent generates article
5. Reviewer agent improves quality
6. Output is displayed + saved (PDF optional)

---


## 🛠️ Installation

```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
pip install -r requirements.txt


▶️ Run the project
python app.py
Then open 
http://127.0.0.1:5000
🔐 Environment Variables

Create a .env file or set system variable:

GROQ_API_KEY=your_api_key_here

📁 Project Structure
ai-agent/
│
├── app.py
├── agents.py
├── search.py
├── memory.py
├── pdf_export.py
├── config.py
└── templates/
    └── index.html


🧠 Tech Stack
Python
Flask
Groq API (LLaMA 3)
DuckDuckGo Search API

🚀 Future Improvements
Online deployment (Render / Vercel)
Advanced UI dashboard
More AI agents (planner, SEO optimizer)
Long-term memory (vector database)
Mobile-friendly version

