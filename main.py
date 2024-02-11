from flask import Flask
from flask import request

app = Flask(name)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/advice', methods=['GET', 'POST'])
def advice():
    if request.method == 'POST':
        data = request.POST
        expenses = float(data.get('expenses'))
        college_costs = float(data.get('college_costs'))
        potential_income = float(data.get('potential_income'))
        money_in_account = float(data.get('money_in_account'))

        total_expenses = expenses + college_costs
        available_money = money_in_account + potential_income

        if available_money >= total_expenses:
            advice = "You have enough funds to cover your expenses next month. You can spend within your budget."
        else:
            additional_funds_needed = total_expenses - available_money
            advice = f"You may need to reconsider your expenses. You are short of ${additional_funds_needed:.2f} to cover your expenses next month."

        return JsonResponse({'advice': advice})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)