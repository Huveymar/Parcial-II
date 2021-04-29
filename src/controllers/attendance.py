# from flask import render_template, request, redirect, url_for
# from src.models.student import Student
# from src.models.session import Session
# from src import app

# @app.route('/attendance/<sessionId>', methods=['GET', 'POST'])
# def attendance(sessionId):
#     sessionModel = Session()
#     studentModel = Student()
#     session = sessionModel.getSession(sessionId)
#     students = studentModel.getStudents()

#     if request.method == 'GET':
#         return render_template('attendance/attendance.html', sessionData=session, students=students, notForm=True)