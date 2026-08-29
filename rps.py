import requests

prompt = """
Choose one: 1, 2, 3, 4, 5, 6, 7, 8, 9
"""

# Choose ONE number:

# 1 = ROCK
# 2 = PAPER
# 3 = SCISSORS

# Answer with only the number.

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "smollm2:135m",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

action = data["response"].strip().upper()

# if action not in ["ROCK", "PAPER", "SCISSORS", "ROCKS"]:
#     print("AI gave an invalid response:", action)
# else :
print("AI:", data["response"])