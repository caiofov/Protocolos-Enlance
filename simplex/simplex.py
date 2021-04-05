

import ../protocol as ptc


class Sender():
  def __init__(self):
    self.s = ptc.Frame() #buffer para um quadro de saída
    self.buffer = ptc.Packet() #buffer para um pacote de saída
    


  def from_network_layer(self, msg):
    self.buffer.info = msg #pega algo para enviar
    
    print("Sender: quadro recebido da camada de rede")

  #enviar para a camada fisica
  def to_physical_layer(self, physical_layer):
    self.s.info = self.buffer; #copia para s, para transmissão
    
    physical_layer.append(self.s) #envia-o para o caminho
    
    print("Sender: quadro enviado para a camada física")


class Receiver():
  def __init__ (self):
    self.r = ptc.Frame()
    self.event = ptc.eventType.frame_arrival #preenchido pela espera, mas não usado aqui
    
    self.network_layer=[]

  #receber da camada fisica
  def from_physical_layer(self, physical_layer):
    self.r = physical_layer.pop(0) #recebe o quadro que chega
    print("Receiver: quadro recebido da camada física")
  
  def to_network_layer(self):
    self.network_layer.apendd(self.r) #passa os dados à camada de rede
    print("Receiver: Pacote enviado à camada de rede")