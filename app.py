from flask import Flask,jsonify,request,g,render_template
# import re
# import bcrypt

# from flask_cors import CORS
# from model.User import User
# from model.Category import Category

# from model.Furniture import Furniture

# from validation.Validator import *

app = Flask(__name__)

# CORS(app)
# http://localhost:5000?data=test@test.com
@app.route('/')
def validate():
    # data = request.args.get('data')
    # pattern = "[a-zA-Z0-9]+@[a-zA-Z-]+\.[a-zA-Z]+"
    # exp = re.compile(pattern)
    # result = "not valid"
    # if (exp.match(data)):
    #     print("valid email")
    #     result = "valid email"
    # else:
    #     print("invalid email")
    #     result = "invalid email"

    #password had to be converted to byte array
    # password = b"12345678"
    # # encode()
    # hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # print("hadhed",hashed)
    # print("salt",bcrypt.gensalt())
    # result = "didnt match"
    # if bcrypt.checkpw(password,hashed):
    #     print("it matches")
    #     result = "it matched"
    # else:
    #     print("didnt match")  
    #     result = "it didnt match"
    result = "hello world!"
    return result

# @app.route('/users/<int:userid>')
# def getUser(userid):
#     try:
#         #print(g.userid)
#         jsonUsers=User.getUser(userid)
#         jsonUsers={"Users":jsonUsers}
#         print("jsonusers",jsonUsers)
#         return jsonify(jsonUsers),200
#     except Exception as err:
#         print(err)
#         return {},500


# @app.route('/users') #define the api route
# def getAllUsers():
#     try:
#         jsonUsers=User.getAllUsers()
#         jsonUsers={"Users":jsonUsers}
#         return jsonify(jsonUsers)
#     except Exception as err:
#         print(err)
#         return {},500



# @app.route('/users', methods=['POST'])
# @validateRegister
# #@login_required
# def insertUsers():
#     print("justin","insertusers")
#     try:
#         userJson=request.json
#         output=User.insertUser(userJson)
#         jsonOutput={"Rows Affected":output}
#         return jsonify(jsonOutput),201
#     except Exception as err:
#         print(err)
#         return {"Rows Affected":0},500




# @app.route('/users/<int:userid>', methods=['PUT'])
# def updateUser(userid):
#     try:
#         userJson=request.json
#         output=User.updateUser(userid,userJson["email"],userJson["password"])
#         jsonOutput={"Rows Affected":output}
#         return jsonify(jsonOutput),200
#     except Exception as err:
#         print(err)
#         return {"Rows Affected":0},500

# @app.route('/users/<int:userid>', methods=['DELETE'])
# def deleteUser(userid):
#     try:
#         userJson=request.json
#         output=User.deleteUser(userid)
#         jsonOutput={"Rows Affected":output}
#         return jsonify(jsonOutput),200
#     except Exception as err:
#         print(err)
#         return {"Rows Affected":0},500


# @app.route('/category') #define the api route
# def getAllCategory():
#     try:
#         jsonCat=Category.getAllCategory()
#         jsonCat={"Category":jsonCat}
#         return jsonify(jsonCat),200
#     except Exception as err:
#         print(err)
#         return {},500


# @app.route('/category/<int:catid>/furniture')
# def getFurnitureByCatId(catid):
#     try:
#         jsonFurniture=Furniture.getFurnitureByCatID(catid)
#         jsonFurniture={"Furniture":jsonFurniture}
#         return jsonify(jsonFurniture),200
#     except Exception as err:
#         print(err)
#         return {},500



# @app.route('/users/login', methods=['POST'])
# def loginUser():
#     try:
#         userJson=request.json
#         output=User.loginUser(userJson)
#         #print(output)
#         return jsonify(output)
#     except Exception as err:
#         print(err)
#         return {},500


# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Web App with Python Flask!'

if __name__ == '__main__':
    app.run(debug=True)
