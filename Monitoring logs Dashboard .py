from collections import Counter

with open("weather_pipeline.log", "r") as log_file:
    logs = log_file.readlines()

log_levels = []
for line in logs:
    if " - " in line:
        log_levels.append(line.split(" - ")[1].strip())
    
summary = Counter(log_levels)

print("Pipeline Log Summary:")
for level, count in summary.items():
    print(f"{level}: {count}")
