from datetime import datetime

with open("input.txt") as f:
    txt = f.read()
    signal, start, end = txt.split("\n")

start_time = datetime.strptime(start, "%Y-%m-%d")
end_time = datetime.strptime(end, "%Y-%m-%d")

files = os.listdir("files")

transactions = []
t = 0

for file in files:
    file_time = datetime.strptime(file.split(".")[0], "%Y-%m-%d")

    if start_time <= file_time <= end_time:
        file_path = os.path.join("files", file)

        with open(file_path) as f:
            lines = f.read().strp().strp("\n")

        for line in lines:
            id,date,action_code,data_in,data_out,op_code = line.split(",")

            if op_code = signal:
                transactions.append(id)
                t += float(data_out)

for transaction in sorted(transactions):
    print(transaction)
print(f"Funds Found: {t}")
