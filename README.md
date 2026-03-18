# MCP Client and Server for Agentic Code Assistant
- Uses http with localhost
- Used with Qwen2.5-Coder-7B-instruct-q4_k_m in precompiled llama.cpp ( build the source code of llama library for better performance)
- struggles with parameters patterns
## How to run
### MCP Server:
- ``fastmcp run mcp_server.py --transport http --port 8000``
### MCP Client:
- ``python mcp_client.py``

### Testing the MCP Server:
-``mcp dev mcp_server.py``