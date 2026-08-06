## 1. Overview

A brief summary covering audio signal processing for ML, hands-on Python implementations, and basic NLP word embeddings.

---

## 2. Audio Signal Processing Fundamentals

### Physics & Perception

* **Sound Waves:** Mechanical pressure waves categorized as **periodic** (harmonics) or **aperiodic** (noise).
* **Key Attributes:** Amplitude, frequency (Hz), and phase.
* **Pitch & Loudness:** Frequency is physical; pitch is perceptual (logarithmic). Loudness (dB) depends on frequency and duration, peaking in human sensitivity between 2–5 kHz.
* **Timbre:** Sound identity shaped by the ADSR envelope and harmonic content.

### Digitalization (ADC / DAC)

* **Sampling & Quantization:** Discretizes time and amplitude.
* **Nyquist Theorem:** Max frequency = $\text{sample rate} / 2$; exceeding this causes aliasing.
* **Bit Depth:** Controls dynamic range (16-bit $\approx$ 96 dB range).

### Feature Extraction & Domains

* **Time-Domain:** Waveforms. Key features include **AE** (onset detection), **RMS** (loudness), and **ZCR** (voiced/unvoiced speech detection).
* **Frequency-Domain:** Spectrum via FFT ($O(N \log_2 N)$ complexity reduction over DFT). Framing and windowing (e.g., Hann) prevent spectral leakage.
* **Time-Frequency Domain:** Spectrograms via STFT (trades off time vs. frequency resolution).
* **Mel Spectrograms & MFCCs:**
* **Mel Scale:** Warps Hz to mirror non-linear human pitch perception.
* **MFCCs:** Formed by applying DCT to the log-Mel spectrum, decorrelating features to capture the vocal tract envelope. Standard vector: 13 static + 13 delta + 13 delta-delta = **39 features/frame**.



---

## 3. Digital Audio Formats

| Format | Type | Encoding | Key Use Case |
| --- | --- | --- | --- |
| **WAV / AIFF** | Uncompressed | PCM (raw samples) | Recording, editing, mastering |
| **MP3** | Lossy | Psychoacoustic masking | Streaming, podcasts |
| **FLAC / ALAC** | Lossless | Linear prediction + Rice coding | High-fidelity archiving |

---

## 4. Practical Implementation Skills

* **Audio Pipelines (`librosa`):** Built end-to-end extraction scripts for AE, RMS, ZCR, FFT, STFT, Mel Spectrograms, and MFCCs (with deltas).
* **Tone Generation:** Wrote a CLI tool generating synthetic sine-wave `.wav` files to test feature pipelines.
* **NLP Fundamentals (`spaCy`):** Extracted word/sentence embeddings, calculated cosine similarity, ran nearest-neighbor searches, and visualized semantic spaces with PCA.

---

## 5. Key Takeaways

* **Solid Foundation:** Clear grasp of sound physics, digital audio tradeoffs, and signal transformation pipelines.
* **Practical Toolkit:** Hands-on experience extracting core audio features for speech and sound ML applications.
* **NLP Bridge:** Early exposure to word embeddings laying the groundwork for multimodal speech-to-text models.
