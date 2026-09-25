import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestMeetingAssistant(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_meeting_processing(self):
        res = self.client.post("/process-meeting", json={
            "meeting_title": "Architecture Sync",
            "transcript_text": "Bilal: We need to finalize the vector search benchmarks by Friday."
        })
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreater(len(data["action_items"]), 0)
        self.assertIn("Bilal", data["action_items"][0]["assignee"])

if __name__ == "__main__":
    unittest.main()
