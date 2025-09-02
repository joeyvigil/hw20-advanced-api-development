from app.blueprints.inventory import inventory_bp
from .schemas import inventory_schema, inventorys_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Inventory, db

# Assignment
# POST '/': Pass in all the required information to create the inventory.
@inventory_bp.route('', methods=['POST']) 
def create_inventory():
    try:
        data = inventory_schema.load(request.json) # type: ignore
    except ValidationError as e:
        return jsonify(e.messages), 400 
    

    new_inventory = Inventory(**data) 
    db.session.add(new_inventory)
    db.session.commit()
    return inventory_schema.jsonify(new_inventory), 201

# Assignment
# GET '/': Retrieves all service tickets.
@inventory_bp.route('', methods=['GET']) 
def read_inventory():
    inventory = db.session.query(Inventory).all()
    return inventorys_schema.jsonify(inventory), 200


# GET at ID
@inventory_bp.route('<int:inventory_id>', methods=['GET'])
def get_at_id_inventory(inventory_id):
    inventory = db.session.get(Inventory, inventory_id)
    return inventory_schema.jsonify(inventory), 200


# Delete at ID
@inventory_bp.route('<int:inventory_id>', methods=['DELETE'])
def delete_inventory(inventory_id):
    try:
        inventory = db.session.get(Inventory, inventory_id)
        db.session.delete(inventory)
        db.session.commit()
        return jsonify({"message": f"Successfully deleted inventory {inventory_id}"}), 200
    except:
        return jsonify({"message": f"Delete of inventory id:{inventory_id} unsuccessful"}), 400


# PUT at id
@inventory_bp.route('<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    inventory = db.session.get(Inventory, inventory_id) 

    if not inventory: 
        return jsonify({"message": "inventory not found"}), 404  
    
    try:
        inventory_data = inventory_schema.load(request.json)  # type: ignore
    except ValidationError as e:
        return jsonify({"message": e.messages}), 400
    
    for key, value in inventory_data.items(): 
        if value: #blank fields will not be updated
            setattr(inventory, key, value) 

    db.session.commit()
    return inventory_schema.jsonify(inventory), 200
    