from project.artifacts.base_artifact import BaseArtifact


class ContemporaryArtifact(BaseArtifact):
        def __init__(self, name: str, price: float, space_required: int):
            super().__init__(name, price, space_required)
        
        def artifact_information(self):
            return f'Contemporary Artifact: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}'


