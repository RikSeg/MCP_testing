import asyncio
import json
from fastmcp import Client
from openai import OpenAI

llm = OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="none"
)

async def main():
    try:
        async with Client("http://localhost:8000/mcp") as mcp:

            tools = await mcp.list_tools()

            tool_schema = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description
                    }
                }
                for t in tools
            ]
            print("Ferramentas disponíveis no MCP Server:")
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")

            messages = [
                {"role": "system", "content": "Seu idioma padrão é Português brasileiro. Use apenas ferramentas para cálculos. Não responda diretamente às perguntas do usuário, apenas chame as ferramentas disponíveis para realizar os cálculos necessários."},
                {"role": "user", "content": "calcule 3 + 5 * (2 - 8)" }
            ]

            while True:
                try:
                    response = llm.chat.completions.create(
                        model="qwen2.5-coder-7b-instruct-q4_k_m",
                        messages=messages,
                        tools=tool_schema,
                    )

                    msg = response.choices[0].message

                    # Append the assistant's message to the conversation
                    messages.append(msg)

                    if not msg.tool_calls:
                        # No more tool calls, print the final response
                        print("Resposta final:", msg.content)
                        break

                    # Process each tool call
                    for call in msg.tool_calls:
                        try:
                            result = await mcp.call_tool(
                                call.function.name,
                                json.loads(call.function.arguments)
                            )
                            print("Tool:", call.function.name)
                            print("Args:", call.function.arguments)
                            # Append the tool result
                            messages.append({
                                "role": "tool",
                                "tool_call_id": call.id,
                                "content": str(result)
                            })
                        except Exception as e:
                            print(f"Erro ao chamar tool {call.function.name}: {e}")
                            # Optionally, append an error message
                            messages.append({
                                "role": "tool",
                                "tool_call_id": call.id,
                                "content": f"Erro: {str(e)}"
                            })
                except Exception as e:
                    print(f"Erro na comunicação com o LLM: {e}")
                    break

    except Exception as e:
        print(f"Erro ao conectar ao servidor MCP: {e}")

asyncio.run(main())