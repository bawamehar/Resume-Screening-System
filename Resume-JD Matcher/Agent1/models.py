from typing import List, Optional
from pydantic import BaseModel, Field

# 1. The Skill Template
class Skill(BaseModel):
    name: str = Field(description="Name of the skill (e.g. Python, SQL, Project Management)")
    context: str = Field(description="Briefly how/where it was used")
    years_of_experience: Optional[int] = Field(description="Years used, if mentioned")
    proficiency: str = Field(description="Level: Beginner, Intermediate, or Expert")

# 2. The Master Template
class ExtractedData(BaseModel):

    job_title: str = Field(description="The formal job title found in the text")
    education: List[str] = Field(description="Degrees, majors, and universities attended")
    tools_and_platforms: List[str] = Field(description="Software, cloud providers, or tools (e.g. AWS, Jira, Tableau)")
    hard_skills: List[Skill] = Field(description="Technical skills and programming languages like python, java, sql, etc.")
    soft_skills: List[Skill] = Field(description="Interpersonal and leadership skills")
    certifications: List[str] = Field(description="Any professional certifications or licenses they have got certified in")
    total_years_experience: float = Field(description="Total years of work experience mentioned")

