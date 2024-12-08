reports = []
safe_reports = []
not_safe_reports = []


with open("./input.txt", "r") as file:
  for line in file:
    if (line):
      line = line.split()
      readings = []
      for reading in line:
        readings.append(int(reading))
      reports.append(readings)

def is_valid(report):
  if len(report) < 2:
     return True
  is_increasing = None

  for reading in range(1, len(report)):
    prev_reading = report[reading - 1]
    current_reading = report[reading]

    difference = abs(current_reading - prev_reading)

    if difference < 1 or difference > 3:
      return False
    
    if is_increasing is None:
      is_increasing = current_reading > prev_reading
    elif is_increasing != (current_reading > prev_reading):
      return False
      
  return True

def is_valid_by_removal(report):
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if is_valid(temp_report):
            return True
    return False

        


for report in reports:
  if is_valid(report):
    safe_reports.append(report)
  else:
    not_safe_reports.append(report)

for report in not_safe_reports:
  if is_valid_by_removal(report):
    safe_reports.append(report)

print(len(safe_reports))
print(len(not_safe_reports))


