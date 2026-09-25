from pydantic import BaseModel
from typing import List, Optional

class MeetingTranscript(BaseModel):
    meeting_title: str
    transcript_text: str

class ActionItem(BaseModel):
    assignee: str
    task: str
    deadline: str

class MeetingMinutes(BaseModel):
    meeting_title: str
    executive_summary: str
    decisions: List[str]
    action_items: List[ActionItem]
    follow_up_email: str
