# ==========================================
# STUDENT-SPECIFIC INPUTS
# ==========================================
LAST_NAME = "Mahinay"
STUDENT_ID = "TUPM-26-4014"
SEED_NUM = int(STUDENT_ID [-1])
FAVORITE_ARTIST = "AVRIL LAVIGNE"

# ==========================================================
# EXERCISE 2: STUDENT PERFORMANCE DATA ANALYZER
# ==========================================================
print("\n------------------------------------------------------------")
print("EXERCISE 2: STUDENT PERFORMANCE DATA ANALYZER")
print("------------------------------------------------------------")

student_names = [f"{LAST_NAME}_Student1", f"{LAST_NAME}_Student2", f"{LAST_NAME}_Student3", f"{LAST_NAME}_Student4", f"{LAST_NAME}_Student5"]

raw_performance_records = [
    {"student": student_names[0], "subject": "PROGRAMMING", "score": 88},
    {"student": student_names[1], "subject": "MATHEMATICS", "score": 75},
    {"student": student_names[2], "subject": "ELECTRONICS", "score": 92},
    {"student": student_names[3], "subject": "PHYSICS", "score": 68},
    {"student": student_names[4], "subject": "ENGLISH", "score": 85},
    {"student": student_names[0], "subject": "PHYSICS", "score": None}, # Incomplete Record
    {"student": student_names[0], "subject": "PROGRAMMING", "score": 88}  # Repeated Record
]

print("\n--- Exercise 2 Assessment Data ---")

# 1. Generated Performance Records
print("\n1. Generated Performance Records:")
for i, rec in enumerate(raw_performance_records, 1):
    print(f"   Record {i}: {rec}")

# 2. Organized Student/Subject Data
organized_students = {}
for rec in raw_performance_records:
    stu = rec["student"]
    if stu not in organized_students:
        organized_students[stu] = {}
    organized_students[stu][rec["subject"]] = rec["score"]

print("\n2. Organized Student/Subject Data:")
for stu, subs in organized_students.items():
    print(f"   Student: {stu} -> {subs}")

# 3. Repeated/Incomplete Records
incomplete_records = [r for r in raw_performance_records if r["score"] is None]
seen_stu_sub = set()
repeated_perf_records = []
for r in raw_performance_records:
    key = (r["student"], r["subject"], r["score"])
    if r["score"] is not None and key in seen_stu_sub:
        repeated_perf_records.append(r)
    elif r["score"] is not None:
        seen_stu_sub.add(key)

print("\n3. Repeated/Incomplete Records:")
print(f"   Incomplete: {incomplete_records}")
print(f"   Repeated: {repeated_perf_records}")

# 4. Performance Categories
def get_category(score):
    if score is None: return "INCOMPLETE"
    elif score >= 90: return "EXCELLENT"
    elif score >= 75: return "PASSED"
    else: return "FAILED"

categorized_records = [{**r, "category": get_category(r["score"])} for r in raw_performance_records]
print("\n4. Performance Categories:")
for r in categorized_records:
    print(f"   {r['student']} ({r['subject']}) Score: {r['score']} -> Category: {r['category']}")

# 5. Student and Subject Summaries
valid_scores = [r["score"] for r in raw_performance_records if r["score"] is not None]
overall_avg = sum(valid_scores) / len(valid_scores)
print("\n5. Student and Subject Summaries:")
print(f"   Class Overall Average Score: {round(overall_avg, 2)}")

# 6. Ordered Results
ordered_performance = sorted([r for r in raw_performance_records if r["score"] is not None], key=lambda x: x["score"], reverse=True)
print("\n6. Ordered Results (Sorted by Score Descending):")
for i, r in enumerate(ordered_performance, 1):
    print(f"   Rank {i}: {r['student']} | {r['subject']} | Score: {r['score']}")

# Final Output (Exercise 2)
print("\nFinal Output: Final Student Performance Report")
print("=" * 60)
for r in categorized_records:
    print(f"Student: {r['student']:<18} | Subject: {r['subject']:<12} | Score: {str(r['score']):<5} | Cat: {r['category']}")
print("=" * 60)