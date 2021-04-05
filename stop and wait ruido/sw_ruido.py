import ../protocol as ptc
import time


class Sender(): #sender
  def __init__(self):
    self.s = ptc.Frame(kind = ptc.frameKind.data) #quadro que sera enviado
    
    self.buffer = ptc.Packet() #pacote que sera enviado
 
    self.event = None #evento

    self.next_frame_to_send = 1 #número de sequencia do proximo quadro

    self.timer; #timer: será a hora atual em que foi ligado mais o self.timer_limit abaixo
    self.timer_limit = 10 #tempo limite do timer em segundos
    self.timerOn = False #começa desligado
  

  def set_timer(self): #função que verifica se passou o tempo do timer. Deve ser chamada apenas quando o mesmo estiver funcionando
    if self.timerOn: #se tiver ligado
      if (self.timer >= time.time()): #se o timer ainda não tiver expirado
        return True
      
      else:
        print("Sender: o timer expirou")
        self.stop_timer()
        self.event = ptc.eventType.timeout

        return False
    
    else: #se tiver desligado (isso não deve acontecer, pois a função deve ser chamada apenas quando estiver funcionando)
      return None
    
  
  def start_timer(self): #iniciar o timer
    self.timerOn = True #liga o timer
    self.timer = time.time() + self.timer_limit #o timer é a hora atual mais o limite definido em segundos

  def stop_timer(self): #parar o timer
    self.timerOff = False #desliga o timer


  def from_network_layer(self, msg): #receber da camada de rede e prepara o quadro para ser enviado

    self.buffer.info = msg #definir mensagem do pacote

    self.s.seq = self.next_frame_to_send - 1 #definir numero de sequencia do quadro

    self.s.info = self.buffer #definir o dado do quadro

    print("Sender: Pacote recebido da camada de rede")


  def to_physical_layer(self, physical_layer): #enviar para a camda fisica
    physical_layer.append(self.s)
    self.start_timer() #inica o cronometro

    print("Sender: quadro enviado para a camada física")

  

  def from_physical_layer(self, physical_layer): #receber confirmação da camada fisica
    try:
      #recebe o quadro do tipo ACK na camada fisica
      for fr in physical_layer:
        if fr.kind == ptc.frameKind.ack:
          frame = physical_layer.pop(physical_layer.index(fr))
          break

      #se o quadro possuir o mesmo número de sequência do quadro que foi enviado
      if frame.seq == self.next_frame_to_send - 1:
        self.event = ptc.eventType.frame_arrival
        print("Sender: quadro de confirmação correto")
        #a transferência foi feita com sucesso
        self.stop_timer()
      
      #caso contrário
      if frame.seq != self.next_frame_to_send - 1:
        print("Sender: quadro de confirmação errado")
        self.event = ptc.eventType.cksum_err #houve erro
    
    except: #caso ocorra algum erro
     
      print("Sender: quadro de confirmação errado")
      self.event = ptc.eventType.cksum_err #houve erro



class Receiver(): #receiver
  def __init__(self):
    self.r = ptc.Frame() #quadro recebido
    self.s = ptc.Frame(kind=ptc.frameKind.ack) #quadro de confirmação

    self.network_layer=[]

    self.event = None

    self.frame_expected = 0


  def from_physical_layer(self, physical_layer):
    try:
      for fr in physical_layer:
        if fr.kind == ptc.frameKind.data:
          frame = physical_layer.pop(physical_layer.index(fr))
          break
    
      #caso o número de sequencia seja o esperado
      if frame.seq == self.frame_expected:
        self.r = frame #frame recebido
        
        self.event = ptc.eventType.frame_arrival #alterar o evento
        
        self.s.seq = self.frame_expected #mudar a sequência do quadro de confirmação

        self.frame_expected += 1
        print("Receiver: quadro recebido da camada física")
    

      #caso contrario
      else:
        print("Receiver: quadro errado")
        self.event = ptc.eventType.cksum_err #alterar o evento
    
    except: #caso ocorra algum erro
      print("Receiver: quadro errado")
      self.event = ptc.eventType.cksum_err #alterar o evento


      
  #enviar para a camada de rede o quadro
  def to_network_layer(self):
    self.network_layer.append(self.r)
    
    print("Receiver: quadro enviado à camada de rede")

  #enviar para a camada fisica o quadro de confirmacao
  def to_physical_layer(self, physical_layer):
    physical_layer.append(self.s)
    
    print("Receiver: quadro de confirmação enviado")

