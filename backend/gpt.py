import openai

def aiProcess(token, prompt):
    token = token
    openai.api_key = token

    model_engine = 'text-davinci-003'

    print(50*"=")
    print("Estou pensando um pouco, peraí...")
    print(50*"=")

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5
    )

    response = completion.choices[0].text.lower()
    print(response)
    return {"response_gpt" : response}