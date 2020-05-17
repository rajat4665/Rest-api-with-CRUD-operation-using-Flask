from flask import (
  Flask, request, jsonify)
from settings import db, app
from models import User


@app.route('/user', methods=['GET'])
def get_all_users():
    """
    this function is map with /user endpoint and 
    it render all user records using GET Http method
    """
    message = {
      'status': 404,
      'message': 'Something went wrong'
    }
    try:
        data = User.query.with_entities(
          User.id, User.name,
          User.email, User.mobile_number,
          User.password).all()
        message.update({
          'status': 200,
          'message': 'ALl records are fetched',
          'data': data
        })
    except:
        pass
    return jsonify(message)


@app.route('/user/<int:id>', methods=['GET'])
def get_specific_user(id):
    """
    this function is map with /user/pk endpoint and 
    it render specific user records with respect to its pk 
    using GET Http method
    """    
    message = {
      'status': 404,
      'message': 'User not exists'
    }
    data = User.query.with_entities(
      User.id, User.name,
      User.email, User.mobile_number,
      User.password).filter_by(id=id).all()
    if len(data) == 0:
        return jsonify(message)
    message.update({
      'status': 200,
      'message': 'ALl records are fetched',
      'data': data
    })
    return jsonify(message)


@app.route('/user', methods=['POST'])
def create_user():
    """
    this function is map with /user endpoint and 
    it create user records using POST Http method
    """    
    message = {
      'status': 404,
      'message': 'Something went wrong'
      }
    try:
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('pwd', '')
        mobile_number = request.form.get('mobile', '')
        user = User(
          name=name,
          email=email,
          password=password,
          mobile_number=mobile_number
        )
        db.session.add(user)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'User created successfully!!! ',
            'user_id': user.id
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    """
    this function is map with /user/pk endpoint and 
    it update specific user records using PUT Http method
    """  
    message = {
      'status': 404,
      'message': 'user not found'
    }
    try:
        new_name = request.form.get('name', None)
        new_email = request.form.get('email', None)
        new_password = request.form.get('pwd', None)
        new_mobile_number = request.form.get('mobile', None)
        try:
            current_user = User.query.get_or_404(id)
        except:
            return jsonify(message)

        if new_email:
            current_user.email = new_email
        if new_name:
            current_user.name = new_name
        if new_password:
            current_user.password = new_password
        if new_mobile_number:
            current_user.mobile_number = new_mobile_number

        db.session.commit()
        message.update({
          'status': 200,
          'message': 'User details updated successfully!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    this function is map with /user/pk endpoint and 
    it delete specific user records using DELETE Http method
    """  
    message = {
      'status': 404,
      'message': 'user not found'
    }
    try:
        current_user = User.query.get_or_404(id)
        db.session.delete(current_user)
        db.session.commit()
        message.update({
          'status': 200,
          'message': 'user record delete successfully!!! '
        })
    except:
        pass
    resp = jsonify(message)
    return resp


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", debug=True)



