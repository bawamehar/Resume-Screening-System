from typing import List, Optional
from pydantic import BaseModel, Field

# Skills Template
class Skill(BaseModel):
    name: str = Field(description="Name of the skill (e.g. Python, SQL, Project Management)")
    context: str = Field(description="Briefly how/where it was used")
    years_of_experience: Optional[int] = Field(description="Years used, if mentioned")
    proficiency: str = Field(description="Level: Beginner, Intermediate, or Expert")

# Master Template
class ExtractedData(BaseModel):

    job_title: str = Field(description="The formal job title found in the text")
    education: List[str] = Field(description="Degrees, majors, and universities attended")
    tools_and_platforms: List[str] = Field(description="Software, cloud providers, or tools (e.g. AWS, Jira, Tableau)")
    hard_skills: List[Skill] = Field(description="Technical skills and programming languages like python, java, sql, etc.")
    soft_skills: List[Skill] = Field(description="Interpersonal and leadership skills")
    certifications: List[str] = Field(description="Any professional certifications or licenses they have got certified in")
    total_years_experience: float = Field(description="Total years of work experience mentioned")


# Agent 2: Match Result & missing skill Templates
class MissingSkill(BaseModel):
    name: str = Field(description="Skill name found in JD but not in Resume")
    is_dealbreaker: bool = Field(description="True if listed in requirements or 'must haves', or mentioned multiple times, False if a 'plus', or 'good to have, etc'")
    priority: int = Field(description="1 for highest priority, 3 for lowest")

class MatchResults(BaseModel):
    match_score: int = Field(description="0-100 technical alignment score")
    experience_reasoning: str = Field(description="Evaluation of YOE using the 20/50 rule or Detailed logic on YOE match")
    skill_reasoning: str = Field(description="Logic on Must-Have vs Nice-to-Have alignment")
    project_reasoning: str = Field(description="How well projects/tools prove the required competencies and match the JD needs")
    missing_skills: List[MissingSkill] = Field(description="List of missing technical/soft skills") # Priority-sorted list
    score_justification: str = Field(description="Comprehensive breakdown of how the final score was calculated")
    education_reasoning: str = Field(description="How the candidate's degree level and certifications match the JD requirements")
    

