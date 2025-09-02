from app.blueprints.ticket_inventory import ticket_inventory_bp
from .schemas import ticket_inventorys_schema, ticket_inventory_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import TicketInventory, db
from app.util.auth import encode_token, token_required

# Assignment
# PUT '/<ticket_id>/assign-inventory/<inventory-id>: Adds a relationship between a service ticket and the inventorys. (Reminder: use your relationship attributes! They allow you the treat the relationship like a list, able to append a Mechanic to the inventorys list).
@ticket_inventory_bp.route('<int:ticket_id>/assign-inventory/<int:inventory_id>', methods=['POST'])
@token_required 
def create_ticket_inventory(ticket_id, inventory_id):
    print(f"{ticket_id} and {inventory_id}")
    new_ticket_inventory = TicketInventory(ticket_id=ticket_id, inventory_id=inventory_id)
    db.session.add(new_ticket_inventory)
    db.session.commit()
    return ticket_inventory_schema.jsonify(new_ticket_inventory), 201

# Assignment
# PUT '/<ticket_id>/remove-inventory/<inventory-id>: Removes the relationship from the service ticket and the inventory.
@ticket_inventory_bp.route('<int:ticket_id>/remove-inventory/<int:inventory_id>', methods=['DELETE'])
@token_required
def delete_ticket_inventory(ticket_id,inventory_id):
    # ticket_inventory = db.session.get(TicketInventory, ticket_inventory_id)
    ticket_inventory = db.session.query(TicketInventory).filter_by(ticket_id=ticket_id,inventory_id=inventory_id).first()
    db.session.delete(ticket_inventory)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted ticket_inventory "}), 200


# # return all service inventorys
# @ticket_inventory_bp.route('', methods=['GET']) 
# def read_ticket_inventory():
#     ticket_inventory = db.session.query(TicketInventory).all()
#     return ticket_inventory_schema.jsonify(ticket_inventory), 200


# # return service inventory at given id
# @ticket_inventory_bp.route('<int:ticket_inventory_id>', methods=['GET'])
# def read_ticket_inventory(ticket_inventory_id):
#     ticket_inventory = db.session.get(TicketInventory, ticket_inventory_id)
#     return ticket_inventory_schema.jsonify(ticket_inventory), 200



# # update service inventory at given id
# @ticket_inventory_bp.route('<int:ticket_inventory_id>', methods=['PUT'])
# def update_ticket_inventory(ticket_inventory_id):
#     ticket_inventory = db.session.get(TicketInventory, ticket_inventory_id) 

#     if not ticket_inventory: 
#         return jsonify({"message": "ticket_inventory not found"}), 404  
    
#     try:
#         ticket_inventory_data = ticket_inventory_schema.load(request.json)  # type: ignore
#     except ValidationError as e:
#         return jsonify({"message": e.messages}), 400
    
#     for key, value in ticket_inventory_data.items(): 
#         if value: #blank fields will not be updated
#             setattr(ticket_inventory, key, value) 

#     db.session.commit()
#     return ticket_inventory_schema.jsonify(ticket_inventory), 200
    
