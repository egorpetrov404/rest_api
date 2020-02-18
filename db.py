from orator import DatabaseManager

config = {
    'postgresql': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'University',
        'user': '',
        'password': '',
        'prefix': ''
    }
}

db = DatabaseManager(config)


def add_std(name, group):
    return db.table('students').insert_get_id({'studentname': name, 'studentgroup': group})


def add_teach(name):
    return db.table('teachers').insert_get_id({'teachername': name})


def add_gr(name, teacher):
    return db.table('groupss').insert_get_id({'groupname': name, 'groupteacher': teacher})


def get_std(student_id):
    info = db.table('students') \
        .select('students.studentname', 'groupss.groupname', 'teachers.teachername') \
        .join('groupss', 'students.studentgroup', '=', 'groupss.id') \
        .join('teachers', 'groupss.groupteacher', '=', 'teachers.id') \
        .where('students.id', student_id).get().all()
    result = {"student": info}
    return result


def get_gr(group_id):
    info = db.table('students') \
        .select('students.studentname', 'groupss.groupname', 'teachers.teachername') \
        .join('groupss', 'students.studentgroup', '=', 'groupss.id') \
        .join('teachers', 'groupss.groupteacher', '=', 'teachers.id') \
        .where('groupss.id', group_id).get().all()
    result = {"group": info}
    return result


def get_teach(teacher_id):
    info = db.table('students') \
        .select('teachers.teachername', 'students.studentname', 'groupss.groupname') \
        .join('groupss', 'students.studentgroup', '=', 'groupss.id') \
        .join('teachers', 'groupss.groupteacher', '=', 'teachers.id') \
        .where('teachers.id', teacher_id).get().all()
    result = {"teacher": info}
    return result
