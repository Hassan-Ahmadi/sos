from abc import abstractmethod, ABC


class BaseInsuranceService(ABC):

    @abstractmethod
    def create_insurance_policy(self, data):
        raise NotImplementedError("Subclasses must implement this method")
