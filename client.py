# client.py
from a2a_sdk import AgentClient

# 连接到服务端（注意：端口必须和server.py一致）
client = AgentClient("http://localhost:8000")

# 调用calculator的add方法
result = client.call(
    agent_name="calculator",  # 服务端Agent的name
    method="add",             # 要调用的方法名
    a=15,                     # 参数
    b=25
)

print("✅ A2A调用成功！结果：", result)