import tkinter as tk
from tkinter import messagebox
import subprocess

# Função para executar o script externo
def run_script():
    try:
        # Executa o script_CV.py
        result = subprocess.run(['python', 'script_CV.py'], capture_output=True, text=True)
        # Mostra a saída do script em uma caixa de mensagem
        messagebox.showinfo("Output", result.stdout)
    except Exception as e:
        # Mostra qualquer erro em uma caixa de mensagem
        messagebox.showerror("Error", str(e))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Executar Script CV")

# Botão para executar o script
btn_run_script = tk.Button(root, text="Executar script_CV.py", command=run_script)
btn_run_script.pack(pady=20)

# Loop principal do Tkinter
root.mainloop()
