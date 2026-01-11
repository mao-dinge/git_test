# server.py
from a2a import client, server
from langgraph.graph import StateGraph, END
from langgraph.graph.state import State


# 定义一个简单的加法Agent（用LangGraph实现）
class CalculatorAgent(Agent):
    def __init__(self):
        super().__init__(name="calculator", description="Adds two numbers")

    def add(self, a: int, b: int) -> int:
        return a + b


# 创建Agent实例
agent = CalculatorAgent()

# 启动A2A服务器（监听8000端口）
if __name__ == "__main__":
    print("🚀 A2A服务已启动！访问 http://localhost:8000")
    server = AgentServer(agent, port=8000)
    server.run()