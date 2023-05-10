from fastapi import Request, UploadFile


class RegistroForm:
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


class Producto:
    def __init__(self, request: Request):
        self.request: Request = request
        self.nombre_producto: str = None
        self.precio: str = None
        self.marca: str = None
        self.descripcion: str = None
        self.categoria: str = None
        self.stock: str = None
        self.imagen: UploadFile = None
        self.nombre_imagen: str = None
        
    async def get_data(self):
        form = await self.request.form()
        self.nombre_producto = form.get("producto")
        self.precio = form.get("precio")
        self.marca = form.get("marca")
        self.descripcion = form.get("descripcion")
        self.categoria = form.get("categoria")
        self.stock = form.get("stock")
        self.imagen = form.get("file")
        self.nombre_imagen = self.nombre_producto + ".jpg"
       
    # funcion para mostrar los datos en consola(borrar luego de la prueba)
    def __str__(self):
        return f"producto: {self.nombre_producto}\nprecio: {self.precio}\ndescripcion: {self.descripcion}\ncategoria: {self.categoria}\nmarca: {self.marca}\nstock: {self.stock}\nimagen: {self.imagen}"