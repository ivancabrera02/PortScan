import tkinter as tk
import socket
import struct
import fcntl #paquete no disponible para windows, probar en Linux

def scan_ports():
  host = host_entry.get()
  start_port = int(start_port_entry.get())
  end_port = int(end_port_entry.get())
  
  open_ports = []
  for port in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    if result == 0:
      open_ports.append(port)
      # utiliza la función get_service_name para obtener el nombre del servicio
      service_name = get_service_name(port)
      ports_list.insert(tk.END, f"Puerto {port} abierto: {service_name}")
    sock.close()
  return open_ports

def get_service_name(port):
  # utiliza la función getservbyport de la librería socket para obtener el nombre del servicio
  return socket.getservbyport(port)

# crea la ventana principal de tkinter
root = tk.Tk()
root.title("Escáner de puertos")

# crea los widgets de entrada para el host y el rango de puertos
host_label = tk.Label(root, text="Host:")
host_entry = tk.Entry(root)
start_port_label = tk.Label(root, text="Puerto inicial:")
start_port_entry = tk.Entry(root)
end_port_label = tk.Label(root, text="Puerto final:")
end_port_entry = tk.Entry(root)

# crea el botón de escaneo y lo asocia con la función scan_ports
scan_button = tk.Button(root, text="Escanear", command=scan_ports)

# crea la lista de puertos abiertos
ports_list = tk.Listbox(root)

# coloca los widgets en la ventana
host_label.grid(row=0, column=0, sticky="w")
host_entry.grid(row=0, column=1, sticky="w")
start_port_label.grid(row=1, column=0, sticky="w")
start_port_entry.grid(row=1, column=1, sticky="w")
end_port_label.grid(row=2, column=0, sticky="w")
end_port_entry.grid(row=2, column=1, sticky="w")
scan_button.grid(row=3, column=0, columnspan=2, sticky="ew")
ports_list.grid(row=4, column=0, columnspan=2, sticky="ew")

# ajusta el tamaño de la ventana y arranca el bucle principal de tkinter
root.columnconfigure(1, weight=1)
root.mainloop()

