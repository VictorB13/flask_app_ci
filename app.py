from flask import Flask, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AutoLease - Car Leasing</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background-color: #f8f9fa;
        }
        .car-card {
            transition: transform 0.2s;
        }
        .car-card:hover {
            transform: scale(1.03);
        }
    </style>
</head>

<body>

<nav class="navbar navbar-dark bg-dark">
    <div class="container">
        <span class="navbar-brand mb-0 h1">🚗 AutoLease</span>
    </div>
</nav>

<div class="container mt-5">

    <h2 class="text-center mb-4">Choose Your Next Car</h2>

    {% if message %}
        <div class="alert alert-success text-center">
            {{ message }}
        </div>
    {% endif %}

    <div class="row">

        <div class="col-md-4">
            <div class="card car-card">
                <div class="card-body">
                    <h5 class="card-title">Toyota Corolla</h5>
                    <p class="card-text">Monthly: ₪1,900</p>
                    <form method="post">
                        <input type="hidden" name="car" value="Toyota Corolla">
                        <button class="btn btn-primary w-100">Request Offer</button>
                    </form>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card car-card">
                <div class="card-body">
                    <h5 class="card-title">Mazda 3</h5>
                    <p class="card-text">Monthly: ₪2,100</p>
                    <form method="post">
                        <input type="hidden" name="car" value="Mazda 3">
                        <button class="btn btn-primary w-100">Request Offer</button>
                    </form>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card car-card">
                <div class="card-body">
                    <h5 class="card-title">Hyundai Ioniq</h5>
                    <p class="card-text">Monthly: ₪2,300</p>
                    <form method="post">
                        <input type="hidden" name="car" value="Hyundai Ioniq">
                        <button class="btn btn-primary w-100">Request Offer</button>
                    </form>
                </div>
            </div>
        </div>

    </div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        car = request.form.get("car")
        message = f"Your request for {car} has been received. We will contact you shortly."

    return HTML_PAGE.replace(
        "{% if message %}", "" if message else "<!--"
    ).replace(
        "{% endif %}", "" if message else "-->"
    ).replace(
        "{{ message }}", message if message else ""
    )

if __name__ == "__main__":
    app.run(debug=True)
