import ../protocol as ptc

class Sender(): #sender
  def __init__(self):
    self.s = ptc.Frame(kind = ptc.frameKind.data)
    self.buffer = ptc.Packet()
    
    self.physical_layer=[]
    self.event = None
  

  def from_network_layer(self): #receber da camada de rede
    msg = input("Mensagem: ")

    self.buffer.info = msg

    self.s.info = self.buffer

    print("Sender: Pacote recebido da camada de rede")


  def to_physical_layer(self,physical_layer): #enviar para a camada física
    physical_layer.append(self.s)
    print("Sender: quadro enviado para a camada física")


  def from_physical_layer(self, physical_layer): #receber da camada física o quadro de confirmação
    physical_layer.pop(0)
    self.event = ptc.eventType.frame_arrival
    print("Sender: quadro de confirmação recebido")




class Receiver():
  def __init__(self):
    self.r = ptc.Frame() #quadro recebido
    self.s = ptc.Frame(kind = ptc.frameKind.ack) #quadro de confirmação

    self.network_layer=[]

    self.event = None

  def from_physical_layer(self, physical_layer): #receber quadro da camada física
    self.r = physical_layer.pop(0)
    self.event = ptc.eventType.frame_arrival

    print("Receiver: quadro recebido da camada física")

  def to_network_layer(self): #enviar quadro para a camada de rede
    self.network_layer.append(self.r)
    print("Receiver: quadro enviado à camada de rede")


  def to_physical_layer(self, physical_layer): #enviar quadro de confirmação para a camada física
    physical_layer.append(self.s)
    print("Receiver: quadro de confirmação enviado")

