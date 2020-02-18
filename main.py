import db
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/addstudent', methods=['POST'])
def addstudent():
    stud = request.get_json(force=True)

    for param in stud["stud"]:
        name = param["name"]
        group = param["group"]
        jsonify(db.add_std(name, group))

    return jsonify(db.db.table('students') \
                   .select('id') \
                   .where('students.id', '>', 0).get().all())


@app.route('/api/addteacher', methods=['POST'])
def addteacher():
    name = request.get_json(force=True)
    return jsonify(db.add_teach(name['name']))


@app.route('/api/addgroup', methods=['POST'])
def addgroup():
    name = request.get_json(force=True)
    teacher = request.get_json(force=True)
    return jsonify(db.add_gr(name['name'], teacher['teacher']))


@app.route('/api/getstudent/<int:student_id>', methods=['GET'])
def getstudent(student_id):
    return jsonify(db.get_std(student_id))


@app.route('/api/getgroup/<int:group_id>', methods=['GET'])
def getgroup(group_id):
    return jsonify(db.get_gr(group_id))


@app.route('/api/getteacher/<int:teacher_id>', methods=['GET'])
def getteacher(teacher_id):
    return jsonify(db.get_teach(teacher_id))


if __name__ == "__main__":
    app.run(debug=True)
