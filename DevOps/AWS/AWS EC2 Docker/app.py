from flask import Flask, request
import statistics as stats

app = Flask(__name__)

@app.route("/v1/")
def hello():
    return 'This is the API version 1'

@app.route("/v1/mean/")
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
