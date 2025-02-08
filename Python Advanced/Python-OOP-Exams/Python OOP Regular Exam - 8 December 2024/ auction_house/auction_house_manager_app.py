from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector
from project.utils.validation import Validation


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts = []
        self.collectors = []


    def valid_artifact_types(self, artifact_type: str):
        return {
            "RenaissanceArtifact": RenaissanceArtifact,
            "ContemporaryArtifact": ContemporaryArtifact,
        }.get(artifact_type)

    def valid_collector_types(self, collector_type: str):
        return {
            "Museum": Museum,
            "PrivateCollector": PrivateCollector,
        }.get(collector_type)

    def __find_object_by_attribute(self, text: str, attribute: str, collection: list) -> object:
        for obj in collection:
            if getattr(obj, attribute) == text:
                return obj

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        artifact = self.valid_artifact_types(artifact_type)

        if artifact is None:
            raise ValueError("Unknown artifact type!")

        Validation.duplicate_name(artifact_name, "name", self.artifacts, f"{artifact_name} has been already registered!")
        new_artifact = artifact(artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        collector = self.valid_collector_types(collector_type)

        if collector is None:
            raise ValueError("Unknown collector type!")

        Validation.duplicate_name(collector_name, "name", self.collectors, f"{collector_name} has been already registered!")
        new_collector = collector(collector_name)
        self.collectors.append(new_collector)

        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self.__find_object_by_attribute(collector_name, "name", self.collectors)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = self.__find_object_by_attribute(artifact_name, "name", self.artifacts)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

        

    def remove_artifact(self, artifact_name: str):
        artifact = self.__find_object_by_attribute(artifact_name, "name", self.artifacts)
        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        total_collector = [collector.increase_money() for collector in self.collectors if collector.available_money <= max_money]
        return f"{len(total_collector)} collector/s increased their available money."
        

    def get_auction_report(self):
        output = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sum(len(c.purchased_artifacts) for c in self.collectors)}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            "***",
            *[f"{c}" for c in sorted(self.collectors, key=lambda collector: (-len(collector.purchased_artifacts), collector.name))],
        ]

        return "\n".join(output)




# Create an instance of AuctionHouseManagerApp
manager = AuctionHouseManagerApp()
# Register artifacts
print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
print()
# Register collectors
print(manager.register_collector("PrivateCollector", "Josh Smith"))
print(manager.register_collector("Museum", "Louvre"))
print(manager.register_collector("Museum", "Hermitage"))
print()
# Perform purchases
print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
print(manager.perform_purchase("Louvre", "Kohinoor"))
print(manager.perform_purchase("Josh Smith", "Zelda"))
print(manager.perform_purchase("Josh Smith", "The Scream"))
print(manager.perform_purchase("Josh Smith", "Untitled"))
print()
# Remove artifact
print(manager.remove_artifact("The Scream"))
print(manager.remove_artifact("Nonexistent"))
print()
# Start fund-raising campaigns
print(manager.fundraising_campaigns(10000.0))
print()
# Get auction report
print(manager.get_auction_report())
print()

# Remove artifact
print(manager.remove_artifact("Untitled"))