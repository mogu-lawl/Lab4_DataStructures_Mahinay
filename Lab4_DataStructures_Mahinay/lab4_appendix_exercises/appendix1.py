import random

# ==========================================
# STUDENT-SPECIFIC INPUTS
# ==========================================
LAST_NAME = "Mahinay"
STUDENT_ID = "TUPM-26-4014"
SEED_NUM = int(STUDENT_ID [-1])
FAVORITE_ARTIST = "AVRIL LAVIGNE"

# Initialize random seed based on inputs for reproducible generation
random.seed(SEED_NUM + len(FAVORITE_ARTIST))

# ==========================================================
# EXERCISE 1: ENGINEERING TEST DATA ORGANIZER
# ==========================================================
print("------------------------------------------------------------")
print("EXERCISE 1: ENGINEERING TEST DATA ORGANIZER")
print("------------------------------------------------------------")

sources = [f"{LAST_NAME}_T1", f"{LAST_NAME}_T2", f"{LAST_NAME}_T3", f"{LAST_NAME}_T4", f"{LAST_NAME}_T5"]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

raw_test_data = [
    {"source": sources[0], "category": "TEMPERATURE", "value": 24.5},
    {"source": sources[1], "category": "VOLTAGE", "value": 12.0},
    {"source": sources[2], "category": "CURRENT", "value": 1.5},
    {"source": sources[3], "category": "PRESSURE", "value": 101.3},
    {"source": sources[4], "category": "SPEED", "value": 150.0},
    {"source": sources[0], "category": "TEMPERATURE", "value": 26.1},
    {"source": sources[1], "category": "VOLTAGE", "value": 11.8},
    {"source": sources[0], "category": "TEMPERATURE", "value": 24.5} # Repeated Record
]

print("\n--- Exercise 1 Assessment Data ---")

# 1. Generated Test Data
print("\n1. Generated Test Data:")
for i, record in enumerate(raw_test_data, 1):
    print(f"   Record {i}: Source={record['source']}, Category={record['category']}, Value={record['value']}")

# 2. Organized Test Data
organized_test_data = {}
for record in raw_test_data:
    src = record["source"]
    cat = record["category"]
    if src not in organized_test_data:
        organized_test_data[src] = {}
    if cat not in organized_test_data[src]:
        organized_test_data[src][cat] = []
    organized_test_data[src][cat].append(record["value"])

print("\n2. Organized Test Data:")
for src, cats in organized_test_data.items():
    print(f"   Source: {src} -> {cats}")

# 3. Repeated/Distinct Data
seen_records = set()
distinct_test_data = []
repeated_test_data = []
for record in raw_test_data:
    identifier = (record["source"], record["category"], record["value"])
    if identifier in seen_records:
        repeated_test_data.append(record)
    else:
        seen_records.add(identifier)
        distinct_test_data.append(record)

print("\n3. Repeated/Distinct Data:")
print(f"   Distinct Count: {len(distinct_test_data)}")
print(f"   Repeated Records: {repeated_test_data}")

# 4. Numerical and Categorical Summaries
cat_summaries = {}
for cat in categories:
    vals = [r["value"] for r in raw_test_data if r["category"] == cat]
    if vals:
        cat_summaries[cat] = {"count": len(vals), "mean": round(sum(vals)/len(vals), 2), "min": min(vals), "max": max(vals)}

print("\n4. Numerical and Categorical Summaries:")
for cat, stats in cat_summaries.items():
    print(f"   Category {cat}: {stats}")

# 5. Processed Results
processed_results = sorted(distinct_test_data, key=lambda x: x["value"], reverse=True)
print("\n5. Processed Results:")
for i, res in enumerate(processed_results, 1):
    print(f"   Processed {i}: {res}")

# 6. Ordered Results
ordered_results = sorted(processed_results, key=lambda x: x["source"])
print("\n6. Ordered Results:")
for i, res in enumerate(ordered_results, 1):
    print(f"   Ordered {i}: {res}")

# 7. Final Summary
print("\n7. Final Summary:")
print(f"   Total records processed: {len(raw_test_data)} | Unique sources: {len(sources)}")

# Final Output (Exercise 1)
print("\nFinal Output: Final Organized and Summarized Test Dataset")
print("-" * 55)
for src, cats in organized_test_data.items():
    print(f"Source: {src:<15} | Categories & Values: {cats}")
print("-" * 55)