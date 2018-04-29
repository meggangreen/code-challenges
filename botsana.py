def tasksTypes(deadlines, day):

    today, upcoming, later = 0, 0, 0

    for deadline in deadlines:
        if deadline <= day:
            today += 1
        elif day+1 <= deadline <= day+7:
            upcoming += 1
        else:
            later += 1

    return [today, upcoming, later]


def smartAssigning(names, statuses, projects, tasks):

    if not names or False not in statuses:
        return None

    selected = -1  # assign to invalid int to start
    for i in xrange(len(names)):
        # On vacation?
        if statuses[i] is True:
            continue

        if selected < 0:
            selected = i
            continue

        if ((tasks[i] < tasks[selected]) or
                (tasks[i] == tasks[selected] and projects[i] < projects[selected])):
            selected = i

    return names[selected]


from datetime import datetime, timedelta
def recurringTask(firstDate, k, daysOfTheWeek, n):
    """ This got very messy trying to read your bot's mind =) """

    try:
        firstDay = datetime.strptime(firstDate, '%d/%m/%Y')
        if not 1900 <= firstDay.year <= 3999:
            return None
    except:
        return None

    if ( (not (1 <= k <= 20)) or (not (1 <= len(daysOfTheWeek) <= 7)) or (not (1 <= n <= 15)) ):
        return None

    if not len(set(daysOfTheWeek)) == len(daysOfTheWeek):
        return None

    task_dates = []

    # I know there's a better way to make this list
    allDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    i = allDays.index(firstDay.strftime('%A'))
    allDays = allDays[i:] + allDays[:i]

    for weekday in daysOfTheWeek:
        if weekday not in allDays:
            return None

    # try:
    # Rotate list so first day is 0th dayOfTheWeek
    firstDay = datetime.strptime(firstDate, '%d/%m/%Y')
    i = daysOfTheWeek.index(firstDay.strftime('%A'))
    daysOfTheWeek = daysOfTheWeek[i:] + daysOfTheWeek[:i]

    j = 0
    m = n
    while m:
        # first
        for i in range(len(daysOfTheWeek)):
            # if j*7 + day_i >
            try:
                day_i = allDays.index(daysOfTheWeek[i])
                task_date = firstDay + timedelta(j*7 + day_i)
            except:
                return None
            if len(task_dates) < n:
                task_dates.append(task_date.strftime('%d/%m/%Y'))
            else:
                return task_dates
            # Decrease remaining task count
            m -= 1

        j += k  # increase week
    # except:
    #     return task_dates[:n]

    return task_dates[:n]
