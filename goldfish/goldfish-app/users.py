from typing import Dict, Union
import uuid

class UserManager:

    def __init__(self):
        self._users_tokens: Dict[str, Union[str, None]] = {}
        self._users_phrases: Dict[str, Dict[int, str]] = {}
        
    def exists(self, user_id: str) -> bool:
        return user_id in self._users_tokens.keys()
        
    def create(self, user_id: str):
        assert not self.exists(user_id)
        self._users_tokens[user_id] = None
        self._users_phrases[user_id] = {}
        
    def valid_token_for(self, user_id: str, token: str | None) -> bool:
        assert self.exists(user_id)
        return token is not None and self._users_tokens[user_id] == token
        
    def generate_token_for(self, user_id: str) -> str:
        assert self.exists(user_id)
        new_token: str = str(uuid.uuid4())
        self._users_tokens[user_id] = new_token
        return new_token
        
    def get_phrases_for(self, user_id: str) -> Dict[int, str]:
        assert self.exists(user_id)
        return self._users_phrases[user_id]
        
    def add_phrase_for(self, user_id: str, new_phrase: str):
        assert self.exists(user_id)
        phrases = self._users_phrases[user_id]
        new_id: int = 1
        if phrases:
            new_id = max(phrases) + 1
        phrases[new_id] = new_phrase
        
    def delete_token_for(self, user_id: str):
        assert self.exists(user_id)
        self._users_tokens[user_id] = None
        
        
        
