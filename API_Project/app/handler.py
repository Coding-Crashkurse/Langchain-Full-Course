import json
import os

import openai
from dotenv import find_dotenv, load_dotenv


class OpenAIHandler:
    def __init__(self, api_functions, function_definitions, model="gpt-3.5-turbo-0613"):
        load_dotenv(find_dotenv())
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        if openai.api_key is None:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")

        self.api_functions = api_functions
        self.function_definitions = function_definitions
        self.model = model

    def send_message(self, query):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": query}],
            functions=self.function_definitions,
        )
        message = response["choices"][0]["message"]
        return message

    def process_function_call(self, message):
        if message.get("function_call"):
            print(message.get("function_call"))
            function_name = message["function_call"]["name"]
            function_args_json = message["function_call"].get("arguments", {})
            function_args = json.loads(function_args_json)

            api_function = self.api_functions.get(function_name)

            if api_function:
                result = str(api_function(**function_args))
                return function_name, result
            else:
                print(f"Function {function_name} not found")
        return None, None

    def send_response(self, query):
        message = self.send_message(query)
        function_name, result = self.process_function_call(message)

        if function_name and result:
            print("Function call necessary to fulfill users request")
            second_response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": query},
                    message,
                    {
                        "role": "function",
                        "name": function_name,
                        "content": result,
                    },
                ],
            )
            return second_response["choices"][0]["message"]["content"]
        else:
            return message["content"]
