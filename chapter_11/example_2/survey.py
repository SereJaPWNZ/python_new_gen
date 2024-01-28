class AnonymousSurvey:
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.response = []

    def show_question(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, response):
        """Сохраняет один ответ на вопрос."""
        self.response.append(response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.response:
            print(f"- {response}")
