import streamlit as st
import json
import pandas as pd
from pathlib import Path
import School_management_system as sms
from School_management_system import Student, Teacher, data, save, load_database

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="EduPulse - School Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern & Vibrant Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Main Background & Gradient Accents */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Card Component */
    .custom-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .custom-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateY(-2px);
    }
    
    /* Hero Title Banner */
    .hero-banner {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #d946ef 100%);
        border-radius: 20px;
        padding: 32px 40px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 20px 30px -10px rgba(124, 58, 237, 0.4);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-top: 8px;
    }
    
    /* Metric Cards */
    .metric-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 14px;
        padding: 20px 24px;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    .badge-student {
        background: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }
    
    .badge-teacher {
        background: rgba(168, 85, 247, 0.2);
        color: #c084fc;
        border: 1px solid rgba(168, 85, 247, 0.3);
    }

    .badge-grade {
        background: rgba(34, 197, 94, 0.2);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    
    /* Sidebar customization */
    section[data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Streamlit Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39);
        transition: all 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5);
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# Initialize Backend Objects
stud_obj = Student()
teach_obj = Teacher()

# Refresh local database state
current_data = load_database()
students_list = current_data.get("students", [])
teachers_list = current_data.get("teachers", [])

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 15px 0 25px 0;'>
            <div style='font-size: 3rem;'>🏫</div>
            <h2 style='margin: 5px 0 0 0; font-weight: 800; background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>EduPulse</h2>
            <p style='color: #64748b; font-size: 0.85rem; margin: 0;'>OOP Record System</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    menu = st.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "👨‍🎓 Student Management",
            "👩‍🏫 Teacher Management",
            "📈 Analytics & Data"
        ],
        index=0
    )
    
    st.markdown("---")
    st.caption("🔒 System Database: `school_records.json`")
    st.caption("⚡ Powered by Object-Oriented Python & Streamlit")

# ==================== HERO SECTION ====================
st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">School Record Management System</div>
        <div class="hero-subtitle">Interactive Admin Dashboard for Students, Teachers & Academic Performance</div>
    </div>
""", unsafe_allow_html=True)

# ==================== 1. DASHBOARD ====================
if menu == "📊 Dashboard":
    st.subheader("📌 Overview & Key Statistics")
    
    # Calculate stats
    total_students = len(students_list)
    total_teachers = len(teachers_list)
    
    all_grades = []
    for s in students_list:
        for g in s.get("grades", {}).values():
            all_grades.append(g)
            
    avg_system_grade = round(sum(all_grades) / len(all_grades), 1) if all_grades else 0.0
    
    # Top KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-container">
                <div>
                    <div class="metric-label">Total Students</div>
                    <div class="metric-value">{total_students}</div>
                </div>
                <div style="font-size: 2rem;">👨‍🎓</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
            <div class="metric-container">
                <div>
                    <div class="metric-label">Total Teachers</div>
                    <div class="metric-value">{total_teachers}</div>
                </div>
                <div style="font-size: 2rem;">👩‍🏫</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
            <div class="metric-container">
                <div>
                    <div class="metric-label">Grades Recorded</div>
                    <div class="metric-value">{len(all_grades)}</div>
                </div>
                <div style="font-size: 2rem;">📝</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
            <div class="metric-container">
                <div>
                    <div class="metric-label">System Average</div>
                    <div class="metric-value">{avg_system_grade}%</div>
                </div>
                <div style="font-size: 2rem;">⭐</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Views
    tab1, tab2 = st.tabs(["👨‍🎓 Recent Students", "👩‍🏫 Faculty Directory"])
    
    with tab1:
        if students_list:
            df_stud = []
            for s in students_list:
                g = s.get("grades", {})
                avg = round(sum(g.values())/len(g), 1) if g else 0
                df_stud.append({
                    "Roll No": s.get("roll_no"),
                    "Name": s.get("name"),
                    "Age": s.get("age"),
                    "Email": s.get("email"),
                    "Subjects Count": len(g),
                    "Average Grade": f"{avg}%"
                })
            st.dataframe(pd.DataFrame(df_stud), use_container_width=True)
        else:
            st.info("No students registered yet. Navigate to 'Student Management' to add a student.")
            
    with tab2:
        if teachers_list:
            st.dataframe(pd.DataFrame(teachers_list), use_container_width=True)
        else:
            st.info("No teachers registered yet. Navigate to 'Teacher Management' to add a faculty member.")

# ==================== 2. STUDENT MANAGEMENT ====================
elif menu == "👨‍🎓 Student Management":
    st.subheader("👨‍🎓 Student Management Portal")
    
    sub_tab1, sub_tab2, sub_tab3 = st.tabs([
        "➕ Register Student", 
        "📝 Add Marks", 
        "🔍 View Student Profile"
    ])
    
    # --- Register Student ---
    with sub_tab1:
        st.markdown("##### 📝 Register a New Student")
        with st.form("register_student_form", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                s_name = st.text_input("Full Name *", placeholder="e.g. Alex Johnson")
                s_age = st.number_input("Age *", min_value=5, max_value=100, value=15)
            with col_b:
                s_email = st.text_input("Email Address *", placeholder="e.g. alex@school.edu")
                s_roll = st.number_input("Roll Number *", min_value=1, step=1, value=101)
                
            submitted = st.form_submit_button("Register Student")
            if submitted:
                if not s_name or not s_email:
                    st.error("Please fill in all required fields.")
                else:
                    success, msg = stud_obj.register_data(s_name.strip(), int(s_age), s_email.strip(), int(s_roll))
                    if success:
                        st.success(msg)
                        st.toast("🎉 Student registered successfully!")
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")
                        
    # --- Add Marks ---
    with sub_tab2:
        st.markdown("##### 📝 Record Subject Marks")
        if not students_list:
            st.warning("No students available. Please register a student first.")
        else:
            student_options = {f"Roll #{s['roll_no']} - {s['name']}": s['roll_no'] for s in students_list}
            selected_student_str = st.selectbox("Select Student", list(student_options.keys()))
            selected_roll = student_options[selected_student_str]
            
            with st.form("add_marks_form", clear_on_submit=True):
                col_m1, col_m2 = st.columns(2)
                with col_m1:
                    subject = st.text_input("Subject Name *", placeholder="e.g. Mathematics, Science, English")
                with col_m2:
                    marks = st.number_input("Marks Obtains (0 - 100) *", min_value=0, max_value=100, value=85)
                    
                marks_submitted = st.form_submit_button("Add / Update Marks")
                if marks_submitted:
                    if not subject.strip():
                        st.error("Please enter a subject name.")
                    else:
                        success, msg = stud_obj.add_marks_data(selected_roll, subject.strip(), int(marks))
                        if success:
                            st.success(msg)
                            st.toast(f"✅ Marks added for {subject}!")
                            st.rerun()
                        else:
                            st.error(f"❌ {msg}")

    # --- View Profile ---
    with sub_tab3:
        st.markdown("##### 🔍 Lookup Student Record")
        if not students_list:
            st.info("No students registered.")
        else:
            search_roll = st.selectbox("Choose Student Roll Number", [s["roll_no"] for s in students_list])
            s = stud_obj.get_student(search_roll)
            
            if s:
                st.markdown(f"""
                    <div class="custom-card">
                        <span class="badge badge-student">Student Profile</span>
                        <h2 style="margin: 10px 0 5px 0;">{s['name']}</h2>
                        <p style="color: #94a3b8; margin-bottom: 15px;">Roll Number: <strong>#{s['roll_no']}</strong> | Age: <strong>{s['age']}</strong> | Email: <strong>{s['email']}</strong></p>
                    </div>
                """, unsafe_allow_html=True)
                
                grades = s.get("grades", {})
                if grades:
                    col_g1, col_g2 = st.columns([2, 1])
                    with col_g1:
                        st.markdown("###### 📚 Academic Marks Breakdown")
                        df_g = pd.DataFrame([{"Subject": k, "Marks": v} for k, v in grades.items()])
                        st.dataframe(df_g, use_container_width=True)
                    with col_g2:
                        avg_score = round(sum(grades.values()) / len(grades), 1)
                        st.metric("Overall Average Grade", f"{avg_score}%")
                        st.progress(min(avg_score / 100.0, 1.0))
                else:
                    st.warning("No grades recorded yet for this student.")

# ==================== 3. TEACHER MANAGEMENT ====================
elif menu == "👩‍🏫 Teacher Management":
    st.subheader("👩‍🏫 Faculty & Teacher Portal")
    
    t_tab1, t_tab2 = st.tabs(["➕ Register Teacher", "🔍 View Faculty Directory"])
    
    with t_tab1:
        st.markdown("##### 📝 Register a New Faculty Member")
        with st.form("register_teacher_form", clear_on_submit=True):
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                t_name = st.text_input("Full Name *", placeholder="e.g. Dr. Robert Smith")
                t_age = st.number_input("Age *", min_value=20, max_value=90, value=35)
                t_subject = st.text_input("Specialized Subject *", placeholder="e.g. Physics, Mathematics")
            with col_t2:
                t_email = st.text_input("Email Address *", placeholder="e.g. rsmith@school.edu")
                t_empid = st.number_input("Employee ID *", min_value=1, step=1, value=501)
                
            t_submitted = st.form_submit_button("Register Teacher")
            if t_submitted:
                if not t_name or not t_email or not t_subject:
                    st.error("Please fill in all required fields.")
                else:
                    success, msg = teach_obj.register_data(t_name.strip(), int(t_age), t_email.strip(), t_subject.strip(), int(t_empid))
                    if success:
                        st.success(msg)
                        st.toast("🎉 Teacher registered successfully!")
                        st.rerun()
                    else:
                        st.error(f"❌ {msg}")
                        
    with t_tab2:
        st.markdown("##### 👩‍🏫 Registered Teachers")
        if teachers_list:
            for t in teachers_list:
                st.markdown(f"""
                    <div class="custom-card">
                        <span class="badge badge-teacher">Faculty Member</span>
                        <h3 style="margin: 10px 0 5px 0;">{t['name']}</h3>
                        <p style="color: #94a3b8; margin: 0;">Employee ID: <strong>#{t['employee_id']}</strong> | Subject: <strong>{t['subject']}</strong></p>
                        <p style="color: #64748b; font-size: 0.9rem; margin-top: 5px;">📧 {t['email']} | 🎂 Age: {t['age']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No teachers registered yet.")

# ==================== 4. ANALYTICS & DATA ====================
elif menu == "📈 Analytics & Data":
    st.subheader("📈 System Analytics & Raw Records")
    
    st.markdown("##### 📊 Student Average Performance Chart")
    if students_list:
        chart_data = []
        for s in students_list:
            g = s.get("grades", {})
            avg = round(sum(g.values()) / len(g), 1) if g else 0
            chart_data.append({"Student": f"{s['name']} (#{s['roll_no']})", "Average Score": avg})
            
        df_chart = pd.DataFrame(chart_data)
        st.bar_chart(df_chart.set_index("Student"))
    else:
        st.info("No performance data available.")
        
    st.markdown("---")
    st.markdown("##### 💾 Raw Database Content (`school_records.json`)")
    st.json(current_data)
    
    # Download JSON
    st.download_button(
        label="📥 Download school_records.json",
        data=json.dumps(current_data, indent=4),
        file_name="school_records.json",
        mime="application/json"
    )
