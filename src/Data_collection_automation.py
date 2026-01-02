from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
input_path = BASE_DIR / "resources" / "data" / "data.txt"
output_path = BASE_DIR / "resources" / "data" / "report.txt"

def calculate_and_report(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    numbers = []
    for line in lines:
        line = line.strip()
        if line:
            numbers.append(float(line))

    total_sum = sum(numbers)

    if numbers:
        average = total_sum / len(numbers)
    else:
        average = 0

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Сума: {total_sum}, Середнє: {average}")

calculate_and_report(input_path, output_path)