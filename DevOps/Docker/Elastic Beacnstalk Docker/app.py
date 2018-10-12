from flask import Flask, request
import statistics as stats

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello world!'

@app.route("/mean")
def mean():

	n_str = request.args.get('numbers')

	if not n_str:
		return "No 'numbers' parameter given"
	else:
		n_list = n_str.split(',')
		n_list = [int(x) for x in n_list]
		avg = stats.mean(n_list)
		return "Mean for given numbers is: " + str(avg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
