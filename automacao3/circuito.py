import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Criar a figura e o eixo
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Desenhar os componentes

# Bateria
ax.plot([1, 1], [2, 4], color='black', linewidth=2)
ax.plot([1.2, 1.2], [2.2, 3.8], color='black', linewidth=1)

# Fios
ax.plot([1.2, 3], [3, 3], color='black')  # da bateria ao interruptor
ax.plot([3, 3], [3, 4], color='black')    # sobe até o interruptor
ax.plot([3, 4], [4, 4], color='black')    # através do interruptor
ax.plot([4, 4], [4, 3], color='black')    # desce do interruptor
ax.plot([4, 6], [3, 3], color='black')    # até o resistor
ax.plot([6, 6], [3, 2], color='black')    # desce até o LED
ax.plot([6, 7], [2, 2], color='black')    # até o LED
ax.plot([7, 7], [2, 1], color='black')    # desce para o fio de retorno
ax.plot([7, 1.2], [1, 1], color='black')  # volta até a bateria
ax.plot([1.2, 1.2], [1, 2.2], color='black')  # fecha o loop na bateria

# Interruptor
ax.add_patch(patches.Rectangle((3.2, 4), 0.6, 0.2, fill=False))
ax.text(3.4, 4.3, 'Interruptor', ha='center', fontsize=8)

# Resistor
ax.add_patch(patches.Rectangle((5.4, 2.8), 1.2, 0.4, fill=False))
ax.text(6, 3.3, 'Resistor', ha='center', fontsize=8)

# LED
ax.plot([7, 7.3], [2, 2.3], color='red')
ax.plot([7, 6.7], [2, 2.3], color='red')
ax.text(7.5, 2, 'LED', fontsize=8)

# Bateria + e -
ax.text(0.8, 4, '+', fontsize=12)
ax.text(0.8, 2, '-', fontsize=12)

plt.title("Circuito Simples com LED, Resistor, Interruptor e Bateria", fontsize=10)
plt.tight_layout()
plt.show()
mudanca
