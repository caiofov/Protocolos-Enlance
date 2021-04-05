import stop_wait as sw
import ../protocol as ptc

sender = sw.Sender()
receiver =  sw.Receiver()

physical_layer = []

while True:
  sender.from_network_layer()
  sender.to_physical_layer()
  receiver.from_physical_layer(physical_layer)
  
  receiver.to_physical_layer(physical_layer)

  if sender.event == ptc.eventType.frame_arrival:
    continue