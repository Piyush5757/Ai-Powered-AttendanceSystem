import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the subject code provided by your teacher to enroll')
    join_code = st.text_input('Subject Code', placeholder='Eg. CS101')

    if st.button('Enroll now', type='primary', width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                if check.data:
                    st.warning('You are already enrolled in this subject')
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success('Successfully enrolled!')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning('Please enter a subject code')


@st.dialog("Auto Enroll in Subject")
def auto_enroll_dialog(join_code):
    # fixed: auto_enroll_dialog was missing — called from app.py with a join_code from URL params
    st.write(f'You were invited to join a subject with code **{join_code}**. Click below to enroll.')

    if st.button('Enroll now', type='primary', width='stretch'):
        res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
        if res.data:
            subject = res.data[0]
            student_id = st.session_state.student_data['student_id']

            check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
            if check.data:
                st.warning('You are already enrolled in this subject')
            else:
                enroll_student_to_subject(student_id, subject['subject_id'])
                st.success(f"Successfully enrolled in {subject['name']}!")
                st.query_params.clear()  # remove join-code from URL after enrolling
                time.sleep(1)
                st.rerun()
        else:
            st.error(f'No subject found with code "{join_code}". Please check with your teacher.')

    if st.button('Cancel', type='tertiary', width='stretch'):
        st.query_params.clear()
        st.rerun()