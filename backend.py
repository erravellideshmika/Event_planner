import os
from google import genai


def generate_event_plan(
    event_type,
    budget,
    location,
    event_date,
    guests,
    preferences
):
    try:
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            return "Gemini API key is not configured."

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an AI Event Planner.

Create a practical event plan using the following details:

Event Type: {event_type}
Budget: ₹{budget}
Location: {location}
Event Date: {event_date}
Number of Guests: {guests}
Preferences: {preferences}

Give the response in these sections:

1. Event Theme
2. Venue Suggestions
3. Decoration Ideas
4. Food Suggestions
5. Budget Breakdown
6. Event Schedule
7. Preparation Checklist

Keep the estimated costs within the given budget.
Make the suggestions practical and easy to understand.
Clearly mention that prices are estimates.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating event plan: {e}"