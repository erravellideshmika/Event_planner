import streamlit as st
from backend import generate_event_plan


st.set_page_config(
    page_title="AI Event Planner",
    page_icon="🎉",
    layout="centered"
)


st.title("🎉 AI Event Planner")
st.write("Plan your event easily with Artificial Intelligence.")


st.subheader("Enter Event Details")


event_type = st.selectbox(
    "Event Type",
    [
        "Birthday",
        "Wedding",
        "College Fest",
        "Conference",
        "Party",
        "Other"
    ]
)


budget = st.number_input(
    "Budget (₹)",
    min_value=1000,
    value=10000,
    step=1000
)


location = st.text_input(
    "Event Location",
    placeholder="Example: Hyderabad"
)


event_date = st.date_input(
    "Event Date"
)


guests = st.number_input(
    "Number of Guests",
    min_value=1,
    value=50,
    step=1
)


preferences = st.text_area(
    "Additional Preferences",
    placeholder="Example: Vegetarian food, simple decoration..."
)


if st.button("✨ Generate Event Plan"):

    if location.strip() == "":
        st.warning("Please enter the event location.")

    else:
        with st.spinner("AI is creating your event plan..."):

            result = generate_event_plan(
                event_type,
                budget,
                location,
                str(event_date),
                guests,
                preferences
            )

        st.subheader("📋 Your AI Event Plan")

        st.markdown(result)
