from fastapi import Request

class Login:
    def __init__(self, request: Request):
        self.request : Request = request
        self.username : str = None
        self.password : str = None
        
    async def get_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")

    # funcion para mostrar los datos en consola(borrar luego de la prueba)    
    def __str__(self):
        return f"username: {self.username}\npassword: {self.password}"
        
class Registro:
    def __init__(self, request: Request):
        self.request : Request = request
        self.username : str = None
        self.password : str = None
        self.email : str = None
        self.nombre : str = None
        self.apellido  : str = None
        self.telefono   : str = None
        self.direccion   : str = None
        self.ciudad : str = None
        self.provincia : str = None
        self.pais : str = None
        self.codigo_postal : str = None
        
    async def get_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
        self.email = form.get("email")
        self.nombre = form.get("nombre")
        self.apellido = form.get("apellido")
        self.telefono = form.get("telefono")
        self.direccion = form.get("direccion")
        self.ciudad = form.get("ciudad")
        self.provincia = form.get("provincia")
        self.pais = form.get("pais")
        self.codigo_postal = form.get("codigo_postal")

    # funcion para mostrar los datos en consola(borrar luego de la prueba)
    def __str__(self):
        return f"username: {self.username}\npassword: {self.password}\nemail: {self.email}\nnombre: {self.nombre}\napellido: {self.apellido}\ntelefono: {self.telefono}\ndireccion: {self.direccion}\nciudad: {self.ciudad}\nprovincia: {self.provincia}\npais: {self.pais}\ncodigo_postal: {self.codigo_postal}"
       