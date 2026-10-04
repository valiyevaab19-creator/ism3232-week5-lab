import os

LIMIT = 1000
HIGH = 2000

records = [
    {
        "id": 1,
        "name": "Taylor",
        "category": "Travel",
        "amount": 1200,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Jordan",
        "category": "Equipment",
        "amount": 450,
        "status": "Pending",
    },
    {
        "id": 3,
        "name": "Morgan",
        "category": "Software",
        "amount": 3500,
        "status": "Approved",
    },
    {"id": 4, "name": "Riley", "category": "Travel", "amount": 89, "status": "Pending"},
    {
        "id": 5,
        "name": "Alex",
        "category": "Equipment",
        "amount": 2200,
        "status": "Pending",
    },
]


def process_records(items):
    total = 0
    flagged = []
    high_value = []

    for rec in items:
        if rec["status"] == "Pending":
            total += rec["amount"]

            # Rule 1: requests over $1,000 need review.
            if rec["amount"] > LIMIT:
                flagged.append(rec)

            # Rule 2: requests over $2,000 are high-value.
            if rec["amount"] > HIGH:
                high_value.append(rec)
    return total, flagged, high_value


def main():
    total, flagged, high_value = process_records(records)

    print("Pending records:")
    for rec in records:
        if rec["status"] == "Pending":
            print(f"{rec['name']}: ${rec['amount']:,.2f}")

    lines = [
        f"Pending total: ${total:,.2f}",
        f"Needs review: {len(flagged)}",
        f"High-value: {len(high_value)}",
    ]

    print("\nSummary:")
    for line in lines:
        print(line)

    os.makedirs("data", exist_ok=True)
    with open("data/week6_summary.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")

    print("\nRecords needing review:")
    for rec in flagged:
        print(f"  ID {rec['id']}: {rec['name']} - ${rec['amount']:,.2f}")

    print("\nSaved summary to data/week6_summary.txt")


if __name__ == "__main__":
    main()
