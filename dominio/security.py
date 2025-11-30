"""Utilidades de seguridad para hashing de contraseñas"""
import hashlib
import os
import base64


class PasswordHasher:
    """Clase para hashear contraseñas con salt usando SHA-256"""
    
    @staticmethod
    def generate_salt() -> str:
        """Genera un salt aleatorio de 32 bytes"""
        return base64.b64encode(os.urandom(32)).decode('utf-8')
    
    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        """
        Hashea una contraseña con el salt proporcionado.
        
        Args:
            password: Contraseña en texto plano
            salt: Salt para el hash
            
        Returns:
            Hash de la contraseña en formato hexadecimal
        """
        password_salt = f"{password}{salt}".encode('utf-8')
        return hashlib.sha256(password_salt).hexdigest()
    
    @staticmethod
    def verify_password(password: str, salt: str, hashed_password: str) -> bool:
        """
        Verifica si una contraseña coincide con el hash.
        
        Args:
            password: Contraseña en texto plano a verificar
            salt: Salt usado en el hash
            hashed_password: Hash almacenado
            
        Returns:
            True si la contraseña es correcta, False en caso contrario
        """
        return PasswordHasher.hash_password(password, salt) == hashed_password
