import requests
import time
from app.logger.logger import logger
from app.config.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    OPENROUTER_BASE_URL,
)
from app.exceptions import OpenRouterError

def generate_response(prompt):
        logger.info(f"Sending request to OpenRouter using model '{OPENROUTER_MODEL}'")
        start = time.perf_counter()
        try:
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
                timeout=30,
            )
            elapsed = (time.perf_counter() - start)*1000
            logger.info(
                f"OpenRouter responded with {response.status_code} in {elapsed:.2f} ms"
            )

            response.raise_for_status()

            data = response.json()

            logger.info("Succesfully parsed OpenRouter response JSON")

            return data["choices"][0]["message"]["content"]
        
        except requests.RequestException:
              logger.exception("Failed to communicate with OpenRouter API")
              raise OpenRouterError("Failed to communicate with OpenRouter API. Please try again later.")