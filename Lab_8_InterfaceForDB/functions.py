def show_end_time(start_time, time_dict):
    for number, time_list in time_dict.items():
        for _ in range(len(time_list)):
            if start_time == time_list[0]:
                return time_list[1]
