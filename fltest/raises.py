
class DidNotRaise(Exception):
    """Exception for when we expected a certain exception type
    """

class Raises:
    """
    A context manager used to expect an exception, much like pytest.raises()
    """
    def __init__(self, exc: type[Exception]) -> None:
        self._type = exc

    def __enter__(self):
        pass

    def __exit__(self, exc_type: type[BaseException], exc_value, exc_traceback) -> bool:
        if exc_type is None:
            raise DidNotRaise(f"Expected a {self._type.__name__}")
        return exc_type is self._type or issubclass(exc_type, self._type)
