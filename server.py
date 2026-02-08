from fastmcp import FastMCP # type: ignore

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """
    Say hello to someone
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
    )
