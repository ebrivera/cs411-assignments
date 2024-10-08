from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:

    def __init__ (self, migration_id: int, current_date: str, start_date: str, current_location: str, migration_path: MigrationPath, status: str = "scheduled") -> None:
        self.migration_id = migration_id
        self.current_date = current_date
        self.start_date = start_date
        self.current_location = current_location
        self.migration_path = migration_path
        self.status = status
        
    
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass