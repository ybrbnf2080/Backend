from typing import List, Optional
import datetime

from sqlalchemy import delete, insert, select
from models.jobs import Job, JobIn
from db.jobs import Job as jobs
from .base import BaseRepository

class JobRepository(BaseRepository):

    async def create(self, user_id: int, j: JobIn) -> Job:
        job = Job(
            id=0,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            is_active=j.is_active,
        )
        values = {**job.dict()}
        values.pop("id", None)
        query = insert(jobs).values(**values).returning(jobs)
        result = self.database.execute(query).first()
        self.database.commit()
        return Job.parse_obj(result._mapping)

    async def update(self, id: int, user_id: int, j: JobIn) -> Job:
        job = Job(
            id=id,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            is_active=j.is_active,
        )
        values = {**job.dict()}
        values.pop("id", None)
        values.pop("created_at", None)
        query = jobs.update().where(jobs.id==id).values(**values).returning(jobs)
        result = self.database.execute(query).first()
        self.database.commit() 
        return Job.parse_obj(job._mapping)

    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Job]:
        query = select(jobs).limit(limit).offset(skip)
        return self.database.execute(query).scalars().all()
    
    async def delete(self, id: int):
        query = delete(jobs).where(jobs.id==id).returning()
        return self.database.execute(query).first()

    async def get_by_id(self, id: int) -> Optional[Job]:
        query = select(jobs).where(jobs.id==id)
        job = self.database.execute(query).scalars().one()
        if job is None:
            return None
        return Job.parse_obj(job.__dict__)