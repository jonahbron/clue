import re

class Prompt:

    def __init__(self, question):
        self.question = question
        self.response_input = None

    def respond(self, response_input):
        if self.validate(response_input):
            self.response_input = response_input

    def validate(self, value):
        return True

    def satisfied(self):
        return self.response_input != None

    def response(self):
        return self.response_input


class IntegerPrompt(Prompt):

    def __init__(self, question, maximum=float('inf')):
        super().__init__(question)
        self.maximum = maximum

    def validate(self, value):
        return value.isdigit() and int(value) <= self.maximum

    def response(self):
        return int(self.response_input)


class SetPrompt(Prompt):

    def __init__(self, question, answer_set, exclude=[]):
        super().__init__(question)
        self.answer_set = [x for x in answer_set if x not in exclude]

    def validate(self, value):
        matches = []
        query = re.compile(".*?".join(list(value)), re.I)
        for answer in self.answer_set:
            if query.search(str(answer)) != None:
                matches.append(answer)

        if len(matches) == 0:
            print("[{}]".format(", ".join(str(answer) for answer in self.answer_set)))
            return False
        elif len(matches) > 1:
            print("[{}]".format(", ".join(str(answer) for answer in matches)))
            return False
        else:
            self.response_input = matches[0]
            return True

    def respond(self, response_input):
        self.validate(response_input)
