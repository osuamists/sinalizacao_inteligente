# Cálculos de Resistores

## Resistor Limitador de Corrente (LEDs)

### Dados de entrada:
- Tensão GPIO Raspberry Pi: **3.3V**
- Tensão direta LED vermelho: **2.0V**
- Corrente desejada: **10mA (0.01A)**

### Cálculo:

**Tensão sobre o resistor:**
V_resistor = V_gpio - V_led
V_resistor = 3.3V - 2.0V = 1.3V

text

**Resistência necessária (Lei de Ohm):**
R = V / I
R = 1.3V / 0.01A = 130Ω

text

**Valor comercial adotado:** 330Ω (mais próximo disponível)

**Corrente real com 330Ω:**
I = V / R
I = 1.3V / 330Ω ≈ 3.9mA

text

**Conclusão:** Corrente de 3.9mA é suficiente para iluminar o LED 
sem risco de dano ao GPIO (limite: 16mA).

---

## Resistor Pull-Down (Botão)

### Dados de entrada:
- Tensão GPIO: **3.3V**
- Resistência típica pull-down: **10kΩ**

### Cálculo de corrente quando botão pressionado:

I = V / R
I = 3.3V / 10,000Ω = 0.33mA

text

**Conclusão:** Corrente desprezível (0.33mA) não sobrecarrega GPIO.

### Por que 10kΩ?

| Valor | Corrente | Problema |
|-------|----------|----------|
| 100Ω | 33mA | Corrente excessiva (GPIO máx: 16mA) |
| 1kΩ | 3.3mA | OK, mas desperdiça energia |
| 10kΩ | 0.33mA | **IDEAL** - padrão industrial |
| 100kΩ | 0.033mA | Muito alto, leitura instável |

---

## Consumo Total do Sistema

| Componente | Corrente |
|------------|----------|
| LED Vermelho (330Ω) | 3.9mA |
| LED Amarelo (330Ω) | 3.9mA |
| LED Verde (330Ω) | 3.9mA |
| LED Azul (330Ω) | 3.9mA |
| Botão (10kΩ) | 0.3mA |
| Raspberry Pi 4 (idle) | ~600mA |
| **TOTAL MÁXIMO** | **~616mA** |

**Fonte necessária:** 5V @ 3A (fornece margem segura)