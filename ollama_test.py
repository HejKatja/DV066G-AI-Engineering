from ollama import chat

def main(): 
    models = ["lfm3:latest", "lfm3-omni:latest", "qwen3.5:4b" ]
    prompt = "All men are mortal, Socrates is a man, therefore Socrates is mortal?"
    temperatures = [0.0, 0.7]

    for model in models:    
        for temperature in temperatures:
            response = chat(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": temperature}
                )

            with open("data/responses.csv", "a", encoding="utf-8") as file: 
                file.write(f'"====== MODEL: {model} | TEMP: {temperature} ======"\n\n')
                file.write(f'"{response["message"]["content"]}"\n\n\n')
                file.write(f'"Time spent generating the responce:  {response.eval_duration / 1000000000}  seconds"\n\n')
                file.write(f'"Total time for the request:  {response.total_duration / 1000000000}  seconds"\n\n')
                file.write("-" * 50 + "\n\n")


            print(f"Response from {model} is now saved.")          


if __name__ == "__main__":
    main()







