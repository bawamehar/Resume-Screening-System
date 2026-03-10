from typing import List, Optional, TypedDict
from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str = Field(description="Name of the skill (e.g. Python, SQL, Project Management)")
    context: str = Field(description="Briefly how/where it was used")
    years_of_experience: Optional[int] = Field(description="Years used, if mentioned")
    proficiency: str = Field(description="Level: Beginner, Intermediate, or Expert")

class ContactInfo(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Professional email address")
    phone: str = Field(description="Phone number with area code")
    location: Optional[str] = Field(description="City and State/Country")
    linkedin: Optional[str] = Field(description="URL to LinkedIn profile")
    github: Optional[str] = Field(description="URL to GitHub or Portfolio")

# main Template
class ExtractedData(BaseModel):
    contact_info: ContactInfo = Field(description="Candidate's personal and contact details")
    job_title: str = Field(description="The formal job title found in the text")
    education: List[str] = Field(description="Degrees, majors, and universities attended")
    tools_and_platforms: List[str] = Field(description="Software, cloud providers, or tools (e.g. AWS, Jira, Tableau)")
    hard_skills: List[Skill] = Field(description="Technical skills and programming languages like python, java, sql, etc.")
    soft_skills: List[Skill] = Field(description="Interpersonal and leadership skills")
    certifications: List[str] = Field(description="Any professional certifications or licenses they have got certified in")
    total_years_experience: float = Field(description="Total years of work experience mentioned")


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
    

class ATSIssue(BaseModel):
    issue_type: str = Field(description="Category: e.g., 'Formatting', 'Keyword Gap', 'Header', 'font'")
    description: str = Field(description="What is wrong?")
    fix: str = Field(description="Exact steps to fix it (e.g., 'Move skills to a bulleted list')")

class ATSResults(BaseModel):
    ats_score: int = Field(description="0-100 score based on parsability and keyword density")
    found_keywords: List[str] = Field(description="Primary JD keywords found in the resume")
    missing_keywords: List[str] = Field(description="Primary or Secondary JD keywords missing from the resume")
    formatting_warnings: List[ATSIssue] = Field(description="Layout or font or structure warnings")
    overall_verdict: str = Field(description="Short summary: e.g., 'make some changes changes' or 'good to be submitted'")

class ResumeBullet(BaseModel):
    original_context: str = Field(description="The existing bullet or project this relates to")
    suggested_bullet: str = Field(description="The new or modified bullet point optimized for JD and ATS")
    reasoning: str = Field(description="Why this change helps (e.g., 'Adds missing keyword')")

class InterviewPrep(BaseModel):
    question: str = Field(description="The interview question")
    category: str = Field(description="Technical, Behavioral, or Domain-Specific")
    intent: str = Field(description="What the recruiter is actually looking for")
    strategy: str = Field(description="How to answer using any existing projects or in general approach")

class CoachResults(BaseModel):
    top_3_bullets: List[ResumeBullet] = Field(description="3 high-impact resume modifications")
    ats_strategy_points: List[str] = Field(description="Specific steps to fix ATS warnings")
    interview_q_and_a: List[InterviewPrep] = Field(description="3 tailored interview questions based on the JD that are most likely to be asked for this Job")
    final_encouragement: str = Field(description="A brief professional closing note")
    

# THE LANGGRAPH STATE
class AgentState(TypedDict):
    raw_resume: str
    raw_jd: str
    resume_obj: Optional[ExtractedData] 
    jd_obj: Optional[ExtractedData]
    match_results: Optional[MatchResults] 
    ats_results: Optional[ATSResults]     
    coach_results: Optional[CoachResults]     