from abc import ABC, abstractmethod
# АBC - Abstract Base Class

class BaseCRUD(ABC):

    @abstractmethod
    def create(self, obj: object):
        pass

    @abstractmethod
    def read(self, obj_id: int):
        pass

    @abstractmethod
    def update(self, obj_id: int, obj: object):
        pass

    @abstractmethod
    def delete(self, obj_id: int):
        pass
class UserCRUD(BaseCRUD):

    def create(self, obj: object):
        print(f"Create user {obj}")

    def read(self, obj_id):
        print(f"Read user {obj_id}")

    def update(self, obj_id, obj):
        print(f"Update user {obj_id} with {obj}")

    def delete(self, obj_id):
        print(f"Delete user {obj_id}")

crud = UserCRUD()
crud.create("Alice")