from abc import ABC, abstractmethod
from project.validation.validation import Validation


class BaseCampaign(ABC):
    CAMPAIGN_IDS = []

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value: str):
        Validation.is_positive_number(
            value, "Campaign ID must be a positive integer greater than zero.")
        Validation.is_unique(value, self.CAMPAIGN_IDS,
                             f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.CAMPAIGN_IDS.append(value)
        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass

