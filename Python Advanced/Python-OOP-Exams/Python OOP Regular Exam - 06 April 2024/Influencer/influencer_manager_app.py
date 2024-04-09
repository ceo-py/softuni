from project.influencers.standard_influencer import StandardInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign


class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    @property
    def influencer_types(self):
        return {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}

    @property
    def campaign_types(self):
        return {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __find_object_by_attribute(self, text: str, attribute: str, collection: list) -> object:
        for obj in collection:
            if getattr(obj, attribute) == text:
                return obj

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.influencer_types:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self.__find_object_by_attribute(
            username, "username", self.influencers)
        if influencer:
            return f"{username} is already registered."

        self.influencers.append(self.influencer_types[influencer_type](
            username, followers, engagement_rate))

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.campaign_types:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self.__find_object_by_attribute(
            campaign_id, "campaign_id", self.campaigns)

        if campaign:
            return f"Campaign ID {campaign_id} has already been created."
        self.campaigns.append(self.campaign_types[campaign_type](
            campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self.__find_object_by_attribute(
            influencer_username, "username", self.influencers)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = self.__find_object_by_attribute(
            campaign_id, "campaign_id", self.campaigns)

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment <= 0:
            return

        campaign.approved_influencers.append(influencer)
        campaign.budget -= payment
        influencer.campaigns_participated.append(campaign)

        return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        return {campaign: i.reached_followers(campaign.__class__.__name__) for campaign in self.campaigns for i in campaign.approved_influencers}

    def influencer_campaign_report(self, username: str):
        influencer = self.__find_object_by_attribute(
            username, "username", self.influencers)

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        output = ['$$ Campaign Statistics $$']

        for campaign in sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget)):
            output.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {sum(i.reached_followers(campaign.__class__.__name__) for i in campaign.approved_influencers)}")

        return '\n'.join(output)
