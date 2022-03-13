
from flask import Flask, render_template, request, redirect, session
import os
from pathlib import PurePath
import datetime
from datetime import time
app = Flask(__name__)
app.secret_key = "piuhpuiuh938h4nppd98gin3r8ah"


# function to get the date and time
def day_and_time():
    now = datetime.datetime.now()
    t = now.strftime('%H:%M:%S')
    if int(t[0:2])> 12:
     clk = " PM"
    else:
        clk = " AM"
    dt = [now.strftime("%B %d, %Y"), t, clk]
    return dt


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    if "checked_out" in session:
        if session["checked_out"]:
            return redirect("/reset")
    checkout_info = {}
    total_orders = int(request.form["apple"])
    total_orders += int(request.form["blackberry"])
    total_orders += int(request.form["strawberry"])
    total_orders += int(request.form["raspberry"])
    for item in request.form:
        session[item] = request.form[item]
    for item in session:
        checkout_info[item] = session[item]
    dat = day_and_time()
    customer_name = checkout_info["first_name"] + " " + checkout_info["last_name"]
    print(f"Charging {customer_name} for {total_orders} fruits")
    session["checked_out"] = True
    return render_template("checkout.html", checkout_info=checkout_info, total_orders=total_orders, dat=dat)


@app.route('/fruits')
def fruits():
    images = './static/img/'
    images_list = []
    for image in os.listdir(images):
        img_src = os.path.join(images, image)
        img_name = PurePath(image).name[0:-4].title()
        if os.path.isfile(img_src):
            images_list.append({"name": img_name, "scr": img_src})
    for image in images_list:
        session[image["name"] + "_name"] = image["name"]
    return render_template("fruits.html", images_list=images_list)


@app.route("/reset")
def rest():
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
