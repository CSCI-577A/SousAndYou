from flask import Flask

app=Flask("__name__")

@app.route('/recipes/{id}',methods=['GET'])
def get_recipe():
    pass

if __name__ == "__main__":
    app.run(debug=True)