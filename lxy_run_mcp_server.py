# coding: utf-8
# A shortcut to launch OpenManus MCP server, where its introduction also solves other import issues.
from app.mcp.lxy_server import LxyMCPServer
from app.mcp.server import parse_args


if __name__ == "__main__":
    args = parse_args()

    # Create and run server (maintaining original flow)
    server = LxyMCPServer()
    server.run(transport=args.transport)
