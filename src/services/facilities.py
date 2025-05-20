from src.schemas.facilities import AddFacilities
from src.services.base import BaseService


class FacilityService(BaseService):
    async def get_facilities(self):
        return await self.db.facilities.get_all()

    async def create_facility(self, data: AddFacilities):
        facility = await self.db.facilities.add(data)
        await self.db.commit()
        return facility
