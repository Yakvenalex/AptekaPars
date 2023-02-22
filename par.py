import re

def find_motul_series(text):
    brand = "Motul"
    series = ""

    patterns = [
        r"Motul|Мотуль\s+(\d*\s+\S*)",
        r"Motul|Мотуль\s+(\d*v\s+[leле] [mansманс])",
        r"Motul|Мотуль\s+(\d*v\s+HIGH RPM)",
        r"Motul|Мотуль\s+(\d*v\s+POWER RACING)",
        r"Motul|Мотуль\s+(\d*v\s+\S*)",
        r"Motul|Мотуль\s+(SPECIFIC\s*\d+\.\d+)",
        r"Motul|Мотуль\s+(SPECIFIC\s*\d+\w+)",
        r"Motul|Мотуль\s+(SPECIFIC\s*\d+\s*\d*\s*\d*\s*\d*)",
        r"Motul|Мотуль\s+(\w+[-]*\s*\w*\s*\d*\w*\+*\s*\d*\w*)\s*",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            for i in range(1, 20):
                series = match.group(i)
                if series:
                    series = series.upper()
                    break
    return brand, series.upper()



name = 'Моторное масло масло мотуль 100v ле манс'

if re.findall(r'Motul|Мотуль', name, re.I):
    print(find_motul_series(name))