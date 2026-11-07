import csv
import os
import platform
import sys

from ollama import chat

MODELS = ["lfm3:latest", "lfm3-omni:latest", "qwen3.5:4b", "gemma4:e2b"]
PROMPT = "All men are mortal, Socrates is a man, therefore Socrates is mortal?"
TEMPERATURES = [0.0, 1.0]
SEED = 4242
OUTPUT_FILE = "data/results.csv"

FIELDS = [
    "run_by",
    "machine",
    "model",
    "temperature",
    "response",
    "thinking_chars",
    "eval_tokens",
    "eval_seconds",
    "load_seconds",
    "total_seconds",
    "tokens_per_second",
]


def main():
    # Who ran the script, e.g. "python ollama_test.py Mohamed"
    run_by = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    machine = f"{platform.system()} {platform.machine()} {platform.processor()}".strip()

    os.makedirs("data", exist_ok=True)
    new_file = not os.path.exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()

        for model in MODELS:
            for temperature in TEMPERATURES:
                response = chat(
                    model=model,
                    messages=[{"role": "user", "content": PROMPT}],
                    options={"temperature": temperature, "seed": SEED},
                )

                # Ollama reports durations in nanoseconds
                eval_seconds = response.eval_duration / 1e9
                thinking = getattr(response.message, "thinking", None) or ""

                writer.writerow({
                    "run_by": run_by,
                    "machine": machine,
                    "model": model,
                    "temperature": temperature,
                    "response": response.message.content,
                    "thinking_chars": len(thinking),
                    "eval_tokens": response.eval_count,
                    "eval_seconds": round(eval_seconds, 2),
                    "load_seconds": round(response.load_duration / 1e9, 2),
                    "total_seconds": round(response.total_duration / 1e9, 2),
                    "tokens_per_second": round(response.eval_count / eval_seconds, 1),
                })

                print(f"Saved: {model} (temperature {temperature})")


if __name__ == "__main__":
    main()
