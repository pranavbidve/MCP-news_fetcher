from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import json
import os
from bs4 import BeautifulSoup

load_dotenv()
#
mcp = FastMCP('project')

USER_AGENT = "project/1.0"
SERPER_URL="https://google.serper.dev/search"


news_sources = {
    "business": "www.nytimes.com/section/business",
    "tech": "www.bbc.com/news/technology",
    "ai": "www.reuters.com/world",
}

# return web results from serper
async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except (httpx.TimeoutException, httpx.HTTPError):
            return {"organic": []}

# fetch url and return content
async def get_content(url: str):
  async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error"


@mcp.tool()
async def fetch_news(query: str, library: str):
  """
  Search the latest news for a given query and library.
  Supports tech, ai, and business.

  Args:
    query: The query to search for (e.g. "Bloomberg news")
    library: The library to search in (e.g. "tech")

  Returns:
    List of dictionaries containign source URLs and extracted text
  """
  if library not in news_sources:
    raise ValueError(f"Library {library} not supported by this tool")
  
  query = f"site:{news_sources[library]} {query}"
  results = await search_web(query)
  if len(results["organic"]) == 0:
    return "No results found"
  
  text = ""
  for result in results["organic"]:
    text += await get_content(result["link"])
  return text


if __name__ == "__main__":
    mcp.run(transport="stdio")

