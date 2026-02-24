"""Quiz Engine CLI - Interactive quiz with score tracking."""
import random, json

QUIZZES = [
    {"q": "What does CPU stand for?", "a": ["Central Processing Unit","Computer Processing Unit","Core Processing Unit","Central Program Unit"], "c": 0},
    {"q": "Which language is known as the 'mother of all languages' in programming?", "a": ["FORTRAN","COBOL","Assembly","C"], "c": 2},
    {"q": "What does HTML stand for?", "a": ["HyperText Markup Language","High Text Machine Language","HyperText Machine Language","HyperLink Markup Language"], "c": 0},
    {"q": "Which data structure uses LIFO ordering?", "a": ["Queue","Stack","Heap","Tree"], "c": 1},
    {"q": "What is the time complexity of binary search?", "a": ["O(n)","O(n²)","O(log n)","O(1)"], "c": 2},
    {"q": "Which company developed Python?", "a": ["Google","Microsoft","Guido van Rossum (PSF)","Apple"], "c": 2},
    {"q": "What is a 'bit'?", "a": ["8 bytes","Binary digit","Base integer type","Block index table"], "c": 1},
    {"q": "Which protocol is used to send email?", "a": ["FTP","SMTP","HTTP","SSH"], "c": 1},
]

def run_quiz():
    questions = random.sample(QUIZZES, min(5, len(QUIZZES)))
    score = 0
    print("\n🧠 Welcome to Quiz Engine CLI!")
    print("=" * 40)
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for j, ans in enumerate(q["a"]):
            print(f"  {j+1}. {ans}")
        while True:
            try:
                choice = int(input("Your answer (1-4): ")) - 1
                if 0 <= choice <= 3:
                    break
            except ValueError:
                pass
            print("Please enter 1-4")
        if choice == q["c"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Answer: {q['a'][q['c']]}")
    print(f"\n{'='*40}")
    print(f"🏆 Score: {score}/{len(questions)}")
    pct = score / len(questions) * 100
    grade = "A" if pct >= 90 else "B" if pct >= 80 else "C" if pct >= 70 else "D" if pct >= 60 else "F"
    print(f"📊 Grade: {grade} ({pct:.0f}%)")

if __name__ == "__main__":
    while True:
        run_quiz()
        if input("\nPlay again? (y/n): ").lower() != "y":
            break
    print("Thanks for playing!")
