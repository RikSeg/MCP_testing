# MCP Client and Server to test AI tools usage
- Uses fastMCP
- Uses http with localhost
- Tested with Qwen2.5-Coder-7B-instruct-q4_k_m in precompiled llama.cpp ( build the source code of llama library for better performance)
- OBS.: Struggles with parameters patterns
## How to run
### MCP Server:
- ``fastmcp run mcp_server.py --transport http --port 8000``
### MCP Client:
- ``python mcp_client.py``

### Testing the MCP Server:
- ``mcp dev mcp_server.py``