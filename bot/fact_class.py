import requests


class Fact:
    """
    This class created for requesting information from repository,
    which https://cat-fact.herokuapp.com/facts/random by default
    """

    def __init__(self, url='https://cat-fact.herokuapp.com/facts/random'):
        self.url = url

    @property
    def some_fact(self):
        """
        Function making request and return JSON-format file with
        some information which was requested from repository
        :return: JSON-format file
        """
        fact_request = requests.get(self.url)
        fact = fact_request.json()['text']
        return fact