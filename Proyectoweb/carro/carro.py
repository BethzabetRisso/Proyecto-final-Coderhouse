
class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            self.session["carro"] = {}
            self.carro = self.session['carro']
        else:
            self.carro = carro
        

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carro.keys():
            self.carro[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            # self.carro[id]["cantidad"] += 1
            # self.carro[id]["precio"] += str(producto.precio)
        #self.guardar_carro()
            for key, value in self.carro.items():
                if key == producto.id:
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"]= float(value["precio"]) + float(producto.precio)
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carro()

    def restar_producto(self, producto):
        id = str(producto.id)
        if id in self.carro.keys():
            self.carro[id]["cantidad"] -= 1
            self.carro[id]["precio"] -= str(producto.precio)
            #if self.carro[id]["cantidad"] <= 0: self.eliminar(producto)
            #self.guardar_carro


        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"]=float(value["precio"])-producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiarCarro(self):
        self.session["carro"] = {}
        self.session.modified = True
