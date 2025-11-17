"""
Learning Assistant Agent - Built with Claude Agent SDK (Python)

A personal learning assistant that helps you:
- Take and organize learning notes
- Query your knowledge base
- Generate quizzes to test your understanding
- Track your learning progress
"""

import asyncio
import os
from dotenv import load_dotenv
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

# Load environment variables
load_dotenv()

# Configure the Learning Assistant Agent
options = ClaudeAgentOptions(
    model="claude-sonnet-4-5-20250929",

    # Define the agent's personality and capabilities
    system_prompt="""You are a Personal Learning Assistant designed to help users learn effectively.

Your capabilities:
1. **Take Learning Notes**: Save notes from articles, documentation, or any learning material the user shares
2. **Answer Questions**: Query the knowledge base to answer questions about previously learned topics
3. **Generate Quizzes**: Create quizzes to test understanding of learned material
4. **Track Progress**: Help users see what they've learned and identify knowledge gaps

Guidelines:
- Be encouraging and supportive in your teaching approach
- Break down complex topics into digestible pieces
- Use examples and analogies to clarify concepts
- When saving notes, organize them clearly with topics and subtopics
- When generating quizzes, include a mix of difficulty levels
- Always cite sources when referencing saved learning material

File Organization:
- Save all learning notes in the 'learning-notes/' directory
- Organize by topic (e.g., 'learning-notes/python/', 'learning-notes/machine-learning/')
- Use markdown format with clear headings and structure
- Include metadata: date, source, key concepts""",

    # Enable tools the agent needs
    allowed_tools=["filesystem", "web_search", "bash"],

    # Set working directory
    working_directory=os.getcwd(),

    # Permission mode - 'default' requires confirmation for file writes
    permission_mode="default",
)


async def run_learning_assistant():
    """Main function to run the learning assistant"""

    print("🎓 Learning Assistant Agent Started!\n")
    print("Available commands:")
    print("  - 'Save notes about [topic]': Save learning notes")
    print("  - 'What did I learn about [topic]?': Query your knowledge base")
    print("  - 'Quiz me on [topic]': Generate a quiz")
    print("  - 'exit': Quit the assistant\n")

    # Create and connect to the agent
    async with ClaudeSDKClient(options=options) as client:
        # Initial greeting and setup
        initial_prompt = """Hi! I'm ready to start learning. Here's what I'd like you to help me with:

1. I want to learn about the Claude Agent SDK
2. Can you help me take notes as I learn?
3. I'll share articles and documentation with you to summarize and save

Let's start by creating a folder structure for my learning notes."""

        # Send the initial query
        await client.query(initial_prompt)

        # Stream and display the response
        async for message in client.receive_response():
            if message.type == "text":
                print(f"\n🤖 Assistant: {message.content}\n")
            elif message.type == "tool_use":
                print(f"🔧 Using tool: {message.tool_name}")
            elif message.type == "tool_result":
                if hasattr(message, 'error') and message.error:
                    print(f"❌ Tool error: {message.error}")

        # Interactive loop for continued conversation
        print("\n" + "="*60)
        print("💬 You can now chat with your learning assistant!")
        print("Type 'exit' to quit\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Happy learning! Your notes are saved in 'learning-notes/'")
                break

            if not user_input:
                continue

            # Send user query
            await client.query(user_input)

            # Stream and display response
            print()
            async for message in client.receive_response():
                if message.type == "text":
                    print(f"🤖 {message.content}")
                elif message.type == "tool_use":
                    print(f"🔧 Using tool: {message.tool_name}")
            print()


async def demo_mode():
    """Run a demo with predefined examples"""

    print("🎓 Learning Assistant - Demo Mode\n")

    async with ClaudeSDKClient(options=options) as client:

        # Example 1: Save notes
        demo_queries = [
            "Please create a note about Python async/await. Here's what I learned: async/await is used for asynchronous programming in Python. The 'async' keyword defines a coroutine function, and 'await' pauses execution until the awaited task completes.",

            "What did I just learn about Python?",

            "Create a short quiz with 3 questions about async/await in Python",
        ]

        for i, query in enumerate(demo_queries, 1):
            print(f"\n{'='*60}")
            print(f"Demo Query {i}: {query}")
            print('='*60)

            await client.query(query)

            async for message in client.receive_response():
                if message.type == "text":
                    print(f"\n🤖 {message.content}\n")
                elif message.type == "tool_use":
                    print(f"🔧 Using: {message.tool_name}")

            # Pause between queries
            if i < len(demo_queries):
                await asyncio.sleep(1)


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ Error: ANTHROPIC_API_KEY not found in environment variables")
        print("Please create a .env file with your API key:")
        print("  ANTHROPIC_API_KEY=your_key_here")
        exit(1)

    # Run the assistant
    # Use demo_mode() for a quick demonstration
    # Use run_learning_assistant() for interactive mode

    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        asyncio.run(demo_mode())
    else:
        asyncio.run(run_learning_assistant())
