from enum import Enum #não sei se é necessária

class Constantes(Enum): 
  MAX_PKT = 2014 #determina o tamanho do pacote em bytes
  MAX_SEQ = 7
  NR_BUFS = (MAX_SEQ+1)/2

class frameKind(Enum):
  data = "data"
  ack = "ack"
  nak = "nak"

class eventType(Enum): #tipos possiveis de eventos
  frame_arrival="frame_arrival"
  cksum_err="cksum_err"
  timeout="timeout"
  network_layer_ready="network_layer_ready"
  ack_timeout="ack_timeout"


class Packet: #pacote
  def __init__ (self, info = None):
    self.info = info;

class Frame: #quadro
  def __init__ (self, info=None, kind=None, seq=None,ack=None):
    self.info = info; #pacote da camada de rede
    self.kind = kind; #tipo de quadro (data, ack ou nak)
    self.seq = seq;  #número da sequencia
    self.ack = ack; #número de confirmacao
