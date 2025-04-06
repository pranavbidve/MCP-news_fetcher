import asyncio
import os
from main import search_web

async def test_serper():
    print("Testing Serper API...")
    print(f"API Key present: {'SERPER_API_KEY' in os.environ}")
    
    result = await search_web("test query")
    if result and "organic" in result:
        print("API call successful!")
        print(f"Number of results: {len(result['organic'])}")
    else:
        print("API call failed!")
        print("Result:", result)

if __name__ == "__main__":
    asyncio.run(test_serper()) 