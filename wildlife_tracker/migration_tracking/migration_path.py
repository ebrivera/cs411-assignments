from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
class MigrationPath:

    def __init__(self, species: str, start_location: Habitat, path_id: int, destination: Habitat, duration: Optional[int] = None) -> None:
        self.species = species
        self.start_location = start_location
        self.path_id = path_id
        self.destination = destination
        self.duration = duration

    def get_migration_path_details(path_id) -> dict:
        pass
    def upadte_migration_path_details(path_id, **kwargs) -> None:
        pass