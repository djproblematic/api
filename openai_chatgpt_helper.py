import openai

class OpenAIHelper:

    def __init__(self, api_key):
        openai.api_key = api_key

    def get_recommendations(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ви є консультантом зі здоров'я."},
                {"role": "user", "content": f"Надайте конкретні та практичні поради щодо здоров'я на основі наступних даних користувача: {user_input}. Будьте детальними, включаючи рекомендації щодо дієти, фізичних вправ та змін способу життя для покращення серцево-судинного здоров'я та схуднення. Уникайте загальних фраз і дайте конкретні кроки."}
            ],
            max_tokens=2000
        )

        if response.choices:
            advice = response.choices[0].message['content'].strip()
            return advice
        else:
            return "Відповідь від API відсутня."

if __name__ == "__main__":
    api_key = "sk-proj-AyUvfMIMl29CvFoRjBjhT3BlbkFJO70d5tNeDZNLnJt6PVI6"
    user_input = "Вік 25, вага 70 кг, зріст 175 см, сидячий спосіб життя, бажання покращити серцево-судинне здоров'я та схуднути."

    ai_helper = OpenAIHelper(api_key)
    advice = ai_helper.get_recommendations(user_input)
    print("Персоналізовані поради:", advice)
