import streamlit as st
import requests

API = "https://your-render-url.onrender.com"

st.title("Leave Management System")
role = st.sidebar.selectbox("Login as", ["Employee", "Admin"])
emp_id = st.sidebar.number_input("Employee ID", min_value=1, value=1)

if role == "Employee":
    tab1, tab2 = st.tabs(["Apply for Leave", "My Requests"])

    with tab1:
        leave_type = st.selectbox("Leave Type", ["Sick", "Casual", "Annual"])
        start = st.date_input("Start Date")
        end = st.date_input("End Date")
        reason = st.text_area("Reason")
        if st.button("Submit"):
            try:
                r = requests.post(f"{API}/leaves/", json={
                    "employee_id": int(emp_id),
                    "leave_type": leave_type,
                    "start_date": str(start),
                    "end_date": str(end),
                    "reason": reason
                })
                if r.ok:
                    st.success("Leave applied successfully!")
                else:
                    st.error(r.json().get("detail", "Something went wrong"))
            except Exception as e:
                st.error(f"Cannot connect to backend: {e}")

    with tab2:
        try:
            leaves = requests.get(f"{API}/leaves/employee/{int(emp_id)}").json()
            if leaves:
                for l in leaves:
                    st.write(f"**{l['leave_type']}** | {l['start_date']} → {l['end_date']} | Status: **{l['status']}**")
            else:
                st.info("No leave requests found.")
        except Exception as e:
            st.error(f"Cannot connect to backend: {e}")

if role == "Admin":
    st.subheader("All Leave Requests")
    try:
        leaves = requests.get(f"{API}/leaves/").json()
        if leaves:
            for l in leaves:
                col1, col2, col3 = st.columns([4, 1, 1])
                col1.write(f"Emp #{l['employee_id']} — {l['leave_type']} | {l['start_date']} → {l['end_date']} | **{l['status']}**")
                if l["status"] == "Pending":
                    if col2.button("Approve", key=f"a{l['id']}"):
                        requests.patch(f"{API}/leaves/{l['id']}/status", json={"status": "Approved"})
                        st.rerun()
                    if col3.button("Reject", key=f"r{l['id']}"):
                        requests.patch(f"{API}/leaves/{l['id']}/status", json={"status": "Rejected"})
                        st.rerun()
        else:
            st.info("No leave requests yet.")
    except Exception as e:
        st.error(f"Cannot connect to backend: {e}")