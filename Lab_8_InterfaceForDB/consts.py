add_deleting_constraints_string = '''
alter table timetable
drop constraint timetable_subject_id_fkey;

alter table teacher
drop constraint teacher_subject_id_fkey;

{}

alter table timetable
add FOREIGN KEY (subject_id) references subject(id);

alter table teacher
add FOREIGN KEY (subject_id) references subject(id);
'''

time_dict = {
                1: ['09:30', '11:05'],
                2: ['11:20', '12:55'],
                3: ['13:10', '14:45'],
                4: ['15:25', '17:00'],
                5: ['17:15', '18:50']
            }

days_of_weeks_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']

week_list = ["Нечетная неделя", "Четная неделя"]
