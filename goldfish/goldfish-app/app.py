from flask import Flask, jsonify, make_response, request
from users import UserManager
import ast

_app = Flask(__name__)
_user_manager: UserManager = UserManager()

def _is_blank(string: str) -> bool:
    return not (string and string.strip())
    
def _user_logged_in(user_id:str, cookie_raw) -> str | None:
    if _is_blank(cookie_raw):
        return None
    else:
        cookie = ast.literal_eval(cookie_raw)
        user_token = cookie['token']
        if not _is_blank(user_token) and _user_manager.valid_token_for(user_id, user_token):
            return user_token
    return None
    
def _validate_login(user_id, request):
    if _is_blank(user_id) or not _user_manager.exists(user_id):
        response_body = jsonify({'error': user_id + " is either invalid or doesn't exist"})
        return {'body': response_body, 'code': 400}
    user_cookie = request.cookies.get('user')
    user_token = _user_logged_in(user_id, user_cookie)
    if user_token is None:
        response_body = jsonify({'error': user_id + " is not logged in"})
        return {'body': response_body, 'code': 401}
    return {'code': 200}
    

@_app.route('/register', methods=['POST'])
def register_user():
    user_id = request.form.get('user_id')
    response_code = 400
    if _is_blank(user_id):
        register_response_body = jsonify({'error': 'user_id is either nil, empty, or contains only blank characters'})
    elif _user_manager.exists(user_id):
        register_response_body = jsonify({'error': user_id + ' is already registered'})
    else:
        _user_manager.create(user_id)
        register_response_body = jsonify({'registered': user_id + ' is now registered'})
        response_code = 200
    return make_response(register_response_body, response_code)

@_app.route('/login', methods=['POST'])
def login():
    user_id = request.form.get('user_id')
    user_id_valid = True
    if _is_blank(user_id):
        user_id_valid = False
        login_response_body = jsonify({'error': 'user_id is either nil, empty, or contains only blank characters'})
    elif not _user_manager.exists(user_id):
        user_id_valid = False
        login_response_body = jsonify({'error': user_id + ' is not registered'})
    if not user_id_valid:
        return make_response(login_response_body, 400)
    user_cookie = request.cookies.get('user')
    user_token = _user_logged_in(user_id, user_cookie)
    if user_token is not None:
        login_response_body = jsonify({'success': user_id + ' is already logged in'})
    else:
        user_token = _user_manager.generate_token_for(user_id)
        login_response_body = jsonify({'success': user_id + ' logged in'})
    resp = make_response(login_response_body, 200)
    token_value = {'token': user_token}
    resp.set_cookie('user', value=str(token_value))
    return resp
        
@_app.route('/<user_id>/phrases', methods=['GET'])
def phrases(user_id):
    login_check_result = _validate_login(user_id, request)
    if login_check_result['code'] != 200:
        phrases_response_body = login_check_result['body']
    else:
        phrases_response_body = jsonify(_user_manager.get_phrases_for(user_id))
    resp = make_response(phrases_response_body, login_check_result['code'])
    return resp
    
@_app.route('/<user_id>/phrases', methods=['POST'])
def add_phrase(user_id):
    login_check_result = _validate_login(user_id, request)
    if login_check_result['code'] != 200:
        new_phrase_response_body = login_check_result['body']
        response_code = login_check_result['code']
    else:
        new_phrase = request.form.get('new_phrase')
        if _is_blank(new_phrase):
            new_phrase_response_body = jsonify({'error': 'invalid phrase'})
            response_code = 400
        else:
            _user_manager.add_phrase_for(user_id, new_phrase)
            response_code = 200
            new_phrase_response_body = jsonify({'success': 'added phrase ' + new_phrase + ' for user ' + user_id})
    resp = make_response(new_phrase_response_body, response_code)
    return resp
    
@_app.route('/<user_id>/logout', methods=['DELETE'])
def logout(user_id):
    login_check_result = _validate_login(user_id, request)
    if login_check_result['code'] != 200:
        logout_response_body = login_check_result['body']
    else:
        _user_manager.delete_token_for(user_id)
        logout_response_body = jsonify({'success': 'user ' + user_id + ' logged out'})
    resp = make_response(logout_response_body, login_check_result['code'])
    return resp

if __name__ == '__main__':
    _app.run(port = 5678)
