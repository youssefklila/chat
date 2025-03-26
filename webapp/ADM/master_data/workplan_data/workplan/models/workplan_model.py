from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from webapp.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from webapp.database import Base


class WorkPlan(Base):
    __tablename__ = "work_plans"

    id = Column(Integer, primary_key=True, index=True)
    state = Column(String, nullable=False)
    part_master_id = Column(Integer, ForeignKey("part_master.id"), nullable=False)  # Relationship with part number
    workplan_description = Column(String, nullable=True)
    valid_from = Column(Date, nullable=False)
    valid_to = Column(Date, nullable=True)
    alternative_work_plan = Column(String, nullable=True)
    infotext = Column(String, nullable=True)
    locked_by = Column(Integer, nullable=True)  # Locked by a user
    process_type = Column(String, nullable=True)
    items = Column(String, nullable=True)
    source_system = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    edited_on = Column(Date, nullable=True)
    created_on = Column(Date, nullable=False)
    erp_change_number = Column(String, nullable=True)
    workplan_type_id = Column(Integer, ForeignKey("workplan_types.id"),
                               nullable=False)  # Relationship with work plan type

    # Relationships
    part_masters = relationship("PartMaster", back_populates="work_plans")
    workplan_type = relationship("WorkPlanType", back_populates="work_plans")
    user = relationship("User", back_populates="work_plans")

    def __repr__(self):
        return f"<WorkPlan(id={self.id}, part_master_id={self.part_master_id}, workplan_type_id={self.workplan_type_id}, state={self.state})>"
