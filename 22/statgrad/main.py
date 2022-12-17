f = open('ege/22/statgrad/data.txt')

processes = {}

for i in f:
    stroka = i.split()
    process_id, process_time = stroka[0], int(stroka[1])
    try:
        affected_processes = stroka[2].split(';')
    except:
        affected_processes = []
    
    processes[process_id] = {
        'time': process_time,
        'affected_by': affected_processes
    }




for proc_id in processes:
    if not processes[proc_id]['affected_by']:
        pass
    else:
        affected_processes_times = []
        for affected_proc_id in processes[proc_id]['affected_by']:
            affected_processes_times.append(processes[affected_proc_id]['time'])
        processes[proc_id]['time'] = processes[proc_id]['time'] + max(affected_processes_times) + 3
    
max_time = 0
for proc_id in processes:
    max_time = max(max_time, processes[proc_id]['time'])

print(max_time)