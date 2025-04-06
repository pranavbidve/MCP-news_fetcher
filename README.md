# 📰 MCP News Fetcher

A Python tool built with MCP framework to fetch and extract news articles from major publishers using Serper API.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![MCP](https://img.shields.io/badge/MCP-1.6.0-green.svg)

## 🌟 Features
- **Multi-source scraping**: Fetch from NYTimes (Business), BBC (Tech), and Reuters (World/AI)
- **Clean text extraction**: Removes ads, menus, and other webpage clutter
- **Async-powered**: Fast parallel fetching using `httpx` and `asyncio`
- **MCP integration**: Ready-to-use tool for your MCP agent workflows

## ⚙️ Setup

### Prerequisites
- Python 3.10+
- [Serper API key](https://serper.dev/) (free tier available)

### Installation
```bash
git clone https://github.com/pranavbidve/MCP-news_fetcher.git
cd MCP-news_fetcher
pip install -e .
```

## Tools and Functions

### Main Tools

1. **fetch_news(query: str, library: str)**
   - Searches for news articles based on a query within a specified library/source
   - Supported libraries: "business", "tech", "ai"
   - Returns extracted text from matching articles

### Helper Functions

1. **search_web(query: str)**
   - Performs web searches using Serper API
   - Returns organic search results
   - Handles timeouts and HTTP errors gracefully

2. **get_content(url: str)**
   - Fetches and parses content from a URL
   - Uses BeautifulSoup to extract clean text
   - Handles timeout errors

## Configuration

The project requires the following environment variables:
- `SERPER_API_KEY` - API key for Serper service (https://serper.dev)

Add these to a `.env` file in your project root.

## Dependencies

- httpx - Async HTTP client
- beautifulsoup4 - HTML parsing
- mcp[cli] - Model Content Protocol server
- python-dotenv - Environment variable management

## Usage

### Running the MCP Server

```bash
python main.py

