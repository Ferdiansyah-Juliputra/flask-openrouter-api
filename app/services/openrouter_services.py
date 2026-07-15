import requests
import time
from logger.logger import logger
from config.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    OPENROUTER_BASE_URL,
)


def generate_response(prompt):
    try:
        logger.info(f"Sending request to OpenRouter using model '{OPENROUTER_MODEL}'")
        start = time.perf_counter()
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": OPENROUTER_MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            },
        )
        elapsed = (time.perf_counter() - start)*1000
        logger.info(
            f"OpenRouter responded with {response.status_code} in {elapsed:.2f} ms"
        )

        response.raise_for_status()
        logger.info(f"OpenRouter Status Code: {response.status_code}")

        data = response.json()

        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        logger.exception("HTTP returned an error response")
        raise Exception(f"Error generating response: {e}")
    
    except requests.exceptions.RequestException as e:
        logger.exception("OpenRouter API request failed")
        raise Exception(f"Error generating response: {e}")
    