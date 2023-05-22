import psycopg2

conn = psycopg2.connect(
    database="bvt2203_schedule",
    user="postgres",
    password="pantera377",
    host="localhost",
    port="3228"
)

cursor = conn.cursor()


def show_lesson(day, is_week_even, lesson_number):
    time_dict = {
        1: ['09:30', '11:05'],
        2: ['11:20', '12:55'],
        3: ['13:10', '14:45'],
        4: ['15:25', '17:00'],
        5: ['17:15', '18:50']
    }
    start_time, end_time = time_dict[lesson_number][0], time_dict[lesson_number][1]
    cursor.execute(
        "SELECT timetable.subject_name, teacher.full_name, timetable.room FROM timetable "
        "JOIN teacher on timetable.subject_name = teacher.subject_name "
        "WHERE start_time='{}' AND day='{}' "
        "AND is_week_even={}".format(start_time, day, is_week_even)
    )
    list1 = list(cursor.fetchall())

    if lesson_number == 1:
        sl_result = "\n{}. {} - {}".format(lesson_number, start_time, end_time)
    else:
        sl_result = "\n\n{}. {} - {}".format(lesson_number, start_time, end_time)
    if len(list1) == 0:
        sl_result += "\n<Нет пары>"
    else:
        subject_name = list1[0][0]
        teacher_name = list1[0][1]
        room = list1[0][2]

        sl_result += "\n{}".format(subject_name)
        sl_result += "\n{}".format(teacher_name)
        sl_result += "\nЛекция в {}.".format(room)
    return sl_result


def show_day_schedule(does_participate_in_week_function, day, is_week_even):
    if not does_participate_in_week_function:
        sds_result = '\nРасписание. {}.'.format(day)
        if is_week_even:
            sds_result += '\nБВТ2203, четная неделя.'
        else:
            sds_result += '\nБВТ2203, нечетная неделя.'
    else:
        sds_result = '\n\n{}'.format(day)
    sds_result += '\n--------------------------------'
    for lesson_number in range(1, 6):
        sds_result += show_lesson(day, is_week_even, lesson_number)
    sds_result += '\n--------------------------------'
    return sds_result


def show_week_schedule(is_week_current, is_week_even):
    if is_week_current:
        sws_result = 'Расписание на неделю.'
    else:
        sws_result = 'Расписание на следующую неделю.'
    if is_week_even:
        sws_result += '\nБВТ2203, четная.'
    else:
        sws_result += '\nБВТ2203, нечетная.'

    days_of_weeks_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    for dow in range(5):
        sws_result += show_day_schedule(1, days_of_weeks_list[dow], is_week_even) + '\n'
    return sws_result

