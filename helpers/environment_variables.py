# SyncStation Configuration

SS_TCP_PORT = 54320
SS_HOSTNAME = '192.168.76.1'

# Read more in the docs "SyncStation Protocol.pdf" or "Quattrocento Protocol.pdf"
SS_START_BYTE = int("00001011", 2)
DEVICES = [int("01001001", 2)]  # SS_5_CONTROL_BYTE = int("01001001", 2), SS_6_CONTROL_BYTE = int("01011001", 2)
SS_START_SIGNAL = [SS_START_BYTE, 0, 0, 0, 0]
SS_START_SIGNAL.extend(DEVICES)

# each sessantoquattro has n channels
# + 6 channels of IMU, buffer, and counter
# + 6 channels from sync station ports and counter
CHANNELS = 70 + 70 + 6 if len(SS_START_SIGNAL) == 7 else 70 + 6

# Quattrocento Configuration
QC_TCP_PORT = 23456
QC_HOSTNAME = "169.254.1.10"

QC_START_BYTE = int("10001011", 2)

QC_START_SIGNAL = [QC_START_BYTE]
QC_START_SIGNAL.extend([0] * 26)

QC_MULTI_IN1_CONF0, QC_MULTI_IN1_CONF1, QC_MULTI_IN1_CONF2 = 0, int("01101100", 2), int("00000000", 2)  # Grid 10mm, 64

QC_START_SIGNAL.extend([0, QC_MULTI_IN1_CONF1, QC_MULTI_IN1_CONF2, 0, QC_MULTI_IN1_CONF1, QC_MULTI_IN1_CONF2])
QC_START_SIGNAL.extend([0] * 6)

STOP_SIGNAL = [0]
