class StoryException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        