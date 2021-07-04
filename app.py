from flask import Flask, render_template,request
import os
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    from urllib.request import urlopen
    
    
    import json
  
    
    url = "https://cms.mlcs.xyz/api/view/program_sessions/all/"
   
    response = urlopen(url)
    
   
    data_json = json.loads(response.read())
    
    

    program_id = []
    for a in data_json:
        program_id.append(a['Program_ID'])
    print (program_id)

    id_session = []
    for a in data_json:
        id_session.append(a['Session_ID'])
    print (id_session)


    session_title = []
    for a in data_json:
        session_title.append(a['Session_Title'])
    print (session_title)

    p_session = []
    for a in data_json:
        p_session.append(a['Program_Duration'])
    print (p_session)

    p_title = []
    for a in data_json:
        p_title.append(a['Program_Title'])
    print (p_title)


    year = []
    for a in data_json:
        year.append(a['Session_Year'])
    print (year)

    

    return render_template("index.html",session_title=session_title,p_session=p_session,id_session=id_session,p_title=p_title,program_id=program_id,year=year )
@app.route("/teacher", methods=['GET','POST'])
def teacher():
    from urllib.request import urlopen

    import json
   
    
    url = "https://cms.mlcs.xyz/api/view/teaching_staff/all/"
    
    response = urlopen(url)

 
    data_json = json.loads(response.read()) 

    
    teacher_id = []
    for a in data_json:
        teacher_id.append(a['teacher_id'])
    print (teacher_id)

    teacher_name = []
    for a in data_json:
        teacher_name.append(a['teacher_name'])
    print (teacher_name)


    t_designation = []
    for a in data_json:
        t_designation.append(a['teacher_designation'])
    print (t_designation)

    t_type = []
    for a in data_json:
        t_type.append(a['teacher_type'])
    print (t_type)

    t_permanant = []
    for a in data_json:
        t_permanant.append(a['teacher_permanant'])
    print (t_permanant)

    return render_template("teacher.html", teacher_id=teacher_id,teacher_name=teacher_name,t_designation=t_designation,t_type=t_type,t_permanant=t_permanant)
@app.route("/intro", methods=['GET','POST'])
def intro():
 
    program_id = request.form.get("program_id")
    session_title = request.form.get("session_title")
    p_session = request.form.get("p_session")
    id_session = request.form.get("id_session")
    p_title = request.form.get("p_title")
    year = request.form.get("year")
    
    teacher_id = request.form.get("teacher_id")
    teacher_name = request.form.get("teacher_name")
    t_designation = request.form.get("t_designation")
    t_type = request.form.get("t_type")
    p_title = request.form.get("p_title")
    t_permanant = request.form.get("t_permanant")

    
    return render_template("intro.html",session_title=session_title,p_session=p_session,
        id_session=id_session,p_title=p_title,program_id=program_id,year=year,
        teacher_id=teacher_id,teacher_name=teacher_name,t_designation=t_designation,t_type=t_type,t_permanant=t_permanant)
    
 
if __name__ == "__main__":
    app.run(debug=True)
