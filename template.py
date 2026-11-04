"""
RECORD CHECK  -  my version
===========================

Name  :hamza
Lane  :  AI / Cyber / IT      (delete two)
Date  : 28 october

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



#  class Record:
class Record:
    over_limit_count = 0

    def __init__(self,label,value,limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
       """Return OVER LIMIT , WARNING or OK from value and limit."""
       pct = self.value / self.limit * 100
       if pct >= 100:
          return "OVER LIMIT"
       elif pct >= 90:
          return "WARNING"
       else: 
           return "OK"


def load_records(path):
    """ Read label,value,limit lines and return a list of Record objects."""
    records = []
    with open(path)as f:
       for line in f :
           line = line.strip()
           if line == "":
              continue
           label,value,limit = line.split(",")
           records.append(Record(label, float(value),float(limit)))

    return records

records = load_records("records_sample.txt")



for record in records:
    result = record.status()
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f" Value  : {record.value}")
    print(f" Limit  : {record.limit}")
    print(f" Status : {result}") 
    print("=" * 34)
    if result == "OVER LIMIT":
       Record.over_limit_count += 1

    print()
print(f"{Record.over_limit_count} of {len(records)} records are OVER LIMIT")
   




