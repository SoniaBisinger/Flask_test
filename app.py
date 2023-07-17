from flask import Flask, jsonify, request

app = Flask(__name__)

dogs = [
    {"id": 1, "name": "Kira", "date of birth": "05.08.2015"},
    {"id": 2, "name": "Nala", "date of birth": "05.02.2023"}
]
#Homepage
@app.route("/")
def index():
    return "<h2> Hello World </h2>"

#get all the dogs
@app.route("/dogs", methods=["GET"])
def get_dogs():
    return dogs

#get a specified dog
@app.route('/dogs/<int:dog_id>', methods=['GET'])
def dog_detail(dog_id):
    for dog in dogs:
        if dog['id']==dog_id:
            return dog

    return {'error': 'Dog not found'}

#create a dog
@app.route('/dogs', methods=['POST'])
def create_dog():
    new_dog = {"id": len(dogs)+1, "name":request.json["name"], "date of birth":request.json['date of birth']}
    dogs.append(new_dog)
    return new_dog

#update a dog
@app.route('/dogs/<int:dog_id>', methods=['PUT'])
def update_dog(dog_id):
    for dog in dogs:
        if dog['id'] == dog_id:
            dog['name'] = request.json['name']
            dog['date of birth'] = request.json['date of birth']
            return dog
    return {'errore': 'dog not found'}

#delete a dog
@app.route('/dogs/<int:dog_id>', methods=['DELETE'])
def delete_dog(dog_id):
    for dog in dogs:
        if dog['id'] == dog_id:
            dogs.remove(dog)
            return {'data' : "Dog deleted successfully"}
    return {'errore': 'dog not found'}

#Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
