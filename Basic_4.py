import csv
from collections import defaultdict

counts = defaultdict(int)
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)  # 假设第一行为列名，B列的列名为'code'
    for row in reader:
        code = row['code'].strip()  # 去除前后空格（可选）
        counts[code] += 1

# 输出结果
for code, count in counts.items():
    print(f"Code: {code}, 行数: {count}")