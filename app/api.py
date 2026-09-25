from fastapi import FastAPI
from app.config import settings
from app.models import MeetingTranscript, MeetingMinutes, ActionItem
from app.services.meeting_parser import parse_meeting

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/process-meeting", response_model=MeetingMinutes)
def process(mtg: MeetingTranscript):
    summary, decisions, actions_raw, email = parse_meeting(mtg.meeting_title, mtg.transcript_text)
    actions = [ActionItem(**a) for a in actions_raw]
    return MeetingMinutes(
        meeting_title=mtg.meeting_title,
        executive_summary=summary,
        decisions=decisions,
        action_items=actions,
        follow_up_email=email
    )
