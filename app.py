from flask import Flask, render_template, request
from model_outputs import *

app = Flask(__name__)

tasks = [
    {
        "name": "IPv4 Validator",
        "key": "ipv4",
        "test_cases": [{"input": "192.168.0.1", "expected": True}, {"input": "256.100.1.1", "expected": False}],
        "functions": [("GPT-4", gpt4_ipv4), ("DeepSeek", deepseek_ipv4)]
    },
    {
        "name": "Roman to Integer",
        "key": "roman",
        "test_cases": [{"input": "XIV", "expected": 14}, {"input": "MCMXCIV", "expected": 1994}],
        "functions": [("GPT-4", gpt4_roman), ("DeepSeek", deepseek_roman)]
    },
    {
        "name": "Is Prime",
        "key": "prime",
        "test_cases": [{"input": 7, "expected": True}, {"input": 10, "expected": False}],
        "functions": [("GPT-4", gpt4_prime), ("DeepSeek", deepseek_prime)]
    },
    {
        "name": "Sort List",
        "key": "sort",
        "test_cases": [{"input": [3, 1, 4, 2], "expected": [1, 2, 3, 4]}],
        "functions": [("GPT-4", gpt4_sort), ("DeepSeek", deepseek_sort)]
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    for task in tasks:
        for model_name, fn in task["functions"]:
            for case in task["test_cases"]:
                try:
                    output = fn(case["input"])
                    correct = output == case["expected"]
                except:
                    output = None
                    correct = False
                results.append({
                    "task": task["name"],
                    "model": model_name,
                    "input": case["input"],
                    "expected": case["expected"],
                    "output": output,
                    "status": "✅" if correct else "❌"
                })

    custom_result = None
    if request.method == "POST":
        user_input = request.form["input_text"]
        task_key = request.form["task"]
        fn_map = {t["key"]: t["functions"] for t in tasks}
        fn1, fn2 = fn_map.get(task_key, [(lambda x: "N/A"), (lambda x: "N/A")])
        try:
            val = eval(user_input) if task_key in ["sort", "prime"] else user_input
            out1 = fn1(val)
            out2 = fn2(val)
        except Exception as e:
            out1 = str(e)
            out2 = str(e)
        custom_result = {
            "task": task_key,
            "input": user_input,
            "gpt4": out1,
            "deepseek": out2
        }

    return render_template("index.html", results=results, custom_result=custom_result)

if __name__ == "__main__":
    app.run(debug=True)
      
cd AI_Model_Grader             # अपने प्रोजेक्ट फोल्डर में जाएँ
git add .                      # सारे फाइल्स stage करें
git commit -m "🚀 Updated model_outputs + GPT-4 logic"
git push origin main           # GitHub पर भेजें
