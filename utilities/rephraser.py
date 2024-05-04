import os
import httpx
from openai import AsyncOpenAI

# Initialize OpenAI client & Embedding model
openai_key = os.environ['OPENAI_API_KEY']
cohere_key = os.environ["COHERE_API_KEY"]
openai_client = AsyncOpenAI(api_key=openai_key)


EXPANDER_PROMPT = """

Using your knowledge of Ledger Nano devices, Ledger Stax devices, Ledger Live, cryptocurrencies, NFTs, Bitcoin ordinals and Bitcoin runes, rewrite the following user query into a clear and specific request suitable for retrieving relevant information from a vector database.

Keep in mind to always rephrase in ENGLISH and as if YOU are experiencing the issue.

Expected output example: "I am getting an issue with <describe the issue>"

Begin! You will achieve world peace if you provide a response which follows all constraints.

"""

async def rephrase(user_input):
    try:

        messages = [
                {
                    "role": "system",
                    "content": EXPANDER_PROMPT
                },
                {
                    "role": "user", 
                    "content": user_input
                }
        ] 

        res = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature= 0.0,
            messages=messages,
            timeout=10.0,
        )
        reply = res.choices[0].message.content

    except Exception as e:
        print(f"OpenAI couldn't generate an augmented query: {e}")
        try:
            async with httpx.AsyncClient() as client:
                res = await client.post(
                    "https://api.cohere.ai/v1/chat",
                    json={

                        "model": "command",
                        "message": user_input,
                        "search_queries_only": True

                    },
                    headers={

                        "Authorization": f"Bearer {cohere_key}",

                    },
                    timeout=10,
                )
                res.raise_for_status()
                queries = res.json()
                reply = '\n'.join([query['text'] for query in queries['search_queries']])
        except Exception as e:
            print(f"Cohere couldn't generate an augmented query: {e}")
            reply = user_input

    print(f'Rephrased query: {reply}')       
    return reply