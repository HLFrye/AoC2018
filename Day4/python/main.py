from datetime import datetime, time
import re

class LogEntry:
  def __init__(self, log_line):
    m = re.match(r"\[(?P<datetime>.*)\] (?P<msg>.*)", log_line)
    self.logdate = datetime.strptime(m.group('datetime'), "%Y-%m-%d %H:%M")
    self.logmsg = m.group('msg')    

  def is_start_entry(self):
    return self.logmsg.find("begins shift") != -1

class NightRecord:
  def __init__(self, start_entry):
    m = re.match(r"Guard #(?P<id>\d+) begins shift", start_entry.logmsg)
    self.id = int(m.group('id'))
    self.is_awake = True
    self.last_event = time(0, 0)
    self.sleepy_time = 0
    self.sleep_schedule = [0] * 60

  def add_event(self, entry):
    if not self.is_awake:
      self.sleepy_time = self.sleepy_time + (entry.logdate.time().minute - self.last_event.minute)
      for i in range(self.last_event.minute, entry.logdate.time().minute):
        self.sleep_schedule[i] = 1
    self.is_awake = not self.is_awake
    self.last_event = entry.logdate.time()

def most_asleep_minute(night_records):
  minutes = [0] * 60
  for record in night_records:
    for i, is_asleep in enumerate(record.sleep_schedule):
      minutes[i] = minutes[i] + is_asleep
  most_asleep_minute = -1
  most_nights_asleep = -1
  for minute, nights in enumerate(minutes):
    if nights > most_nights_asleep:
      most_asleep_minute = minute
      most_nights_asleep = nights
  return most_asleep_minute, most_nights_asleep

def lookahead(iterable):
  """Pass through all values from the given iterable, augmented by the
  information if there are more values to come after the current one
  (True), or if it is the last value (False).
  """
  # Get an iterator and pull the first value.
  it = iter(iterable)
  last = next(it)
  # Run the iterator to exhaustion (starting from the second value).
  for val in it:
    # Report the *previous* value (more to come).
    yield last, True
    last = val
  # Report the last value.
  yield last, False

def main():
  log_entries = []
  with open('../input.txt') as input:
    for line in input.readlines():
      log_entries.append(LogEntry(line))

  log_entries.sort(key=lambda x: x.logdate)
  
  records = []
  curr_record = None
  for entry, more in lookahead(log_entries):
    if entry.is_start_entry():
      if curr_record is not None:
        records.append(curr_record)
      curr_record = NightRecord(entry)
    else:
      curr_record.add_event(entry)
    if not more:
      records.append(curr_record)

  guard_records = {}
  for record in records:
    if record.id in guard_records:
      guard_records[record.id].append(record)
    else:
      guard_records[record.id] = [record]
  
  sleepy_nights = -1
  sleepy_minute = -1
  sleepy_guard = -1
  for guard_id, records in guard_records.items():
    minute, nights = most_asleep_minute(records)
    if nights > sleepy_nights:
      sleepy_nights = nights
      sleepy_minute = minute
      sleepy_guard = guard_id

  print("The code is {}".format(sleepy_guard * sleepy_minute))

if __name__ == '__main__':
  main()