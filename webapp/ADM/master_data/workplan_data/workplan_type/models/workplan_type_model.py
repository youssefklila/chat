from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from webapp.database import Base

class WorkPlanType(Base):
    __tablename__ = "workplan_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    work_plans = relationship("WorkPlan", back_populates="workplan_type")
    def __repr__(self):
        return f"<WorkPlanType(id={self.id}, name={self.name}, description={self.description})>"
