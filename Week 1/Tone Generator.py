"""
Citation / References:
1- https://github.com/kronengold/tone-generator/blob/master/tonegen.py
2- https://github.com/timbatt/music_maker/blob/master/Tone.py
"""

import argparse
import sys
import wave
import math
import struct

def generate_tone_wav(frequency, duration=5.0, sample_rate=44100, bits=16, output_filename=None):
    if not output_filename:
        freq_str = int(frequency) if frequency.is_integer() else frequency
        output_filename = f"{freq_str}Hz_{duration}s.wav"

    total_samples = int(sample_rate * duration)
    frames_list = []

    for i in range(total_samples):
        t = i / sample_rate
        sample_val = math.sin(2 * math.pi * frequency * t)
        amplitude = 2 ** (bits - 1) - 1 # 32767
        pcm_val = int(round(sample_val * amplitude))

        frames_list.append(struct.pack("<h", pcm_val))

    raw_bytes = b"".join(frames_list)

    with wave.open(output_filename, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(raw_bytes)

    print(f"Saved: {output_filename}")


def main():
    parser = argparse.ArgumentParser(description='Tone Generator using NumPy')
    parser.add_argument('-f', '--frequency', type=float, help='Set frequency in Hz (e.g., 440)', required=False)
    parser.add_argument('-t', '--time', type=float, default=5.0, help='Set duration in seconds (default: 5.0)')
    parser.add_argument('-r', '--samplerate', type=int, default=44100, help='Set sample rate (default: 44100)')
    
    args = parser.parse_args()

    if args.frequency is None:
        if len(sys.argv) == 1:
            print("Usage: python 'Tone Generator.py' -f <frequency_in_hz>")
            print("Example: python 'Tone Generator.py' -f 440")
            sys.exit(1)
        else:
            print("Error: Frequency argument (-f) is required.")
            sys.exit(1)

    generate_tone_wav(
        frequency=args.frequency,
        duration=args.time,
        sample_rate=args.samplerate
    )


if __name__ == "__main__":
    main()
