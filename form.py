from flask import Flask , request,jsonify
from flask_cors import CORS
import pymysql
import pymysql.cursors

# step: 2
app = Flask (__name__)
CORS (app)

#step:3
db_config = {
    "host":"localhost",
    "password":"",
    "user":"root",
    "database":"icecreamform"
}
#step4:
@app.route("/ice_cream",methods = ["GET"])
def ice_cream():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor . execute("select*FROM icecreamtable")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify (rows)

#step:5

@app.route("/ice", methods=["POST"])
def ice():
    booking = request.json
    name = booking["name"]
    email = booking["email"]
    phone = booking["phone"]
    message = booking["message"]  # ✅ fixed this line

    # ✅ This should be inside the function:
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    sql = "INSERT INTO icecreamtable (name, email, phone, message) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, email, phone, message))  # ✅ fixed arguments
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Booking Successful!"})  # ✅ should be inside function

if __name__ == "__main__":
    app.run(debug=True)
