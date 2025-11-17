# 🎓 Learning Assistant Agent

A personal learning assistant built with the Claude Agent SDK (Python) to help you learn more effectively.

## Features

- 📝 **Note-Taking**: Automatically save and organize learning notes from articles, docs, and videos
- 🔍 **Knowledge Base**: Query what you've learned with natural language questions
- 📊 **Quiz Generation**: Test your understanding with AI-generated quizzes
- 📈 **Progress Tracking**: See your learning journey and identify knowledge gaps

## Setup

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Copy `.env.example` to `.env`
   - Add your Anthropic API key from [console.anthropic.com](https://console.anthropic.com/)

4. **Run the agent**:
   ```bash
   # Interactive mode
   python main.py

   # Demo mode (see examples)
   python main.py --demo
   ```

## How to Use

### Save Learning Notes
```
"I just read this article about React hooks: [paste content or URL]"
```

### Query Your Knowledge Base
```
"What did I learn about useState hooks?"
```

### Generate a Quiz
```
"Quiz me on React hooks"
```

## Project Structure

```
learning-assistant-agent/
├── main.py               # Main agent code
├── requirements.txt      # Python dependencies
├── learning-notes/       # Your saved learning notes (created automatically)
├── .env.example          # API key template
├── .gitignore
└── README.md
```

## Learning Path

This project teaches you:
1. **Agent SDK Basics**: Creating and configuring agents
2. **Tool Integration**: Using filesystem, web search, and bash tools
3. **Context Management**: Handling long conversations and memory
4. **System Prompts**: Defining agent behavior and personality
5. **Production Patterns**: Error handling and session management

## Next Steps

- [ ] Run the agent and save your first learning note
- [ ] Query your knowledge base
- [ ] Generate your first quiz
- [ ] Customize the system prompt for your learning style
- [ ] Add custom tools or integrations (MCP)
# learning-_assistant_agent
