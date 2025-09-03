import win32api
import win32con
import keyboard
import time

# Constantes para orientação
DMDO_DEFAULT = 0       # Paisagem normal
DMDO_90 = 1            # Retrato
DMDO_180 = 2           # Paisagem invertida
DMDO_270 = 3           # Retrato invertido

def mudar_orientacao(orientacao):
    device = win32api.EnumDisplayDevices(None, 0)
    dm = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

    atual = dm.DisplayOrientation
    if orientacao in (DMDO_90, DMDO_270) and atual in (DMDO_DEFAULT, DMDO_180):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    elif orientacao in (DMDO_DEFAULT, DMDO_180) and atual in (DMDO_90, DMDO_270):
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

    dm.DisplayOrientation = orientacao

    resultado = win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)
    if resultado == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"✅ Tela girada para orientação {orientacao}.")
    else:
        print(f"❌ Falha ao mudar a orientação. Código de erro: {resultado}")

# Mudar para paisagem invertida
print("🔁 Girando tela para paisagem invertida (180°)...")
mudar_orientacao(DMDO_180)

# Esperar tecla "~" ou "`"
print("⌛ Pressione a tecla '~' ou '`' para restaurar...")
while True:
    if keyboard.is_pressed('`') or keyboard.is_pressed('~'):
        break
    time.sleep(0.1)

# Restaurar orientação normal
print("🔁 Restaurando para paisagem normal...")
mudar_orientacao(DMDO_DEFAULT)
print("🏁 Concluído.")
