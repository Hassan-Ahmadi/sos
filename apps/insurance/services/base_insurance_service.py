from abc import abstractmethod, ABC


class BaseInsuranceService(ABC):

    @abstractmethod
    def process_data(self, data):
        raise NotImplementedError("Subclasses must implement this method")
