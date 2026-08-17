import math

print("======================================")
print("     ADVANCED SPEAKER SYSTEM")
print("======================================")

User inputs

frequency = float(input("Enter audio frequency (Hz): "))
volume = float(input("Enter volume (0-100): "))
bass = float(input("Enter bass level (-10 to +10): "))
treble = float(input("Enter treble level (-10 to +10): "))
gain = float(input("Enter amplifier gain (1-10): "))

Limit values

volume = max(0, min(volume, 100))
bass = max(-10, min(bass, 10))
treble = max(-10, min(treble, 10))
gain = max(1, min(gain, 10))

Amplifier output

amplified_signal = volume * gain

Speaker response

bass_effect = bass * (1 / (1 + frequency / 200))
treble_effect = treble * (frequency / 5000)

final_output = amplified_signal + bass_effect + treble_effect

Protection system

if final_output > 1000:
protection = "OVERLOAD PROTECTION ACTIVE"
else:
protection = "System operating normally"

Frequency range

if frequency < 250:
frequency_type = "Bass"
elif frequency < 4000:
frequency_type = "Mid-range"
else:
frequency_type = "Treble"

print("\n========== SPEAKER STATUS ==========")
print("Frequency       :", frequency, "Hz")
print("Frequency Type  :", frequency_type)
print("Volume          :", volume, "%")
print("Bass Level      :", bass)
print("Treble Level    :", treble)
print("Amplifier Gain  :", gain, "x")
print("Output Level    :", round(final_output, 2))
print("Protection      :", protection)

print("\nAdvanced Features:")
print("✓ Digital Volume Control")
print("✓ Bass & Treble Control")
print("✓ Amplifier Gain")
print("✓ Frequency Detection")
print("✓ Overload Protection")
print("✓ Audio Signal Processing")

print("\nSpeaker simulation completed successfully!")
