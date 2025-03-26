from webapp.ADM.master_data.part_master.repositories.part_master_repository import PartMasterRepository


class PartMasterService:
    def __init__(self, part_master_repository: PartMasterRepository):
        self.part_master_repository = part_master_repository
    def get_all_part_masters(self):
        return self.part_master_repository.get_all()

    def get_part_master_by_id(self, part_master_id: int):
        return self.part_master_repository.get_by_id(part_master_id)

    def create_part_master(self, **kwargs):
        return self.part_master_repository.create(**kwargs)

    def update_part_master(self, part_master_id: int, **kwargs):
        return self.part_master_repository.update(part_master_id, **kwargs)

    def delete_part_master(self, part_master_id: int):
        self.part_master_repository.delete(part_master_id)
