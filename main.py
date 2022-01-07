from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

stocks_tickers = ['AAPL', 'FB', 'GS', 'TSLA', 'BTC']

todos = ['React Project', 'Python Project', 'Blockchain Project']


def stock_function():
    for ticker in stocks_tickers:
        data = web.DataReader(ticker, 'yahoo')
        print(f"The last price of {ticker} was {data['Close'].iloc[-1]}")


def todo_project():
    print("Your TODO List:")
    for todo in todos:
        print(todo)


def todo_add():
    todo = input("Add a Task to TODO List: ")
    todos.append(todo)


def todo_remove():
    idx = int(input("Remove a Task from TODO List: ")) - 1
    if idx < len(todos):
        print(f"Removing {todos[idx]}")
        todos.pop(idx)
    else:
        print("There is no TODO at this position")


def bye():
    print("Bye")
    sys.exit(0)


mappings = {'stocks': stock_function,
            'todoshow': todo_project,
            'todoadd': todo_add,
            'todoremove': todo_remove,
            'goodbye': bye}

assistant = GenericAssistant("intents.json", mappings)

assistant.train_model()
assistant.save_model()

while True:
    message = input("Message: ")
    assistant.request(message)
