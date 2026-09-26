# ⚔️ The Zero-VRAM Gauntlet — Benchmarks

> **📦 This directory has moved.**
>
> All benchmark content, test scripts, and deep-dives now live in the **WERR repository**, where they belong:
>
> ## 👉 [github.com/pCwOrM/werr/tree/main/benchmarks](https://github.com/pCwOrM/werr/tree/main/benchmarks)

---

> 🌐 **Language Switcher / Dil Seçici:**  
> **English (Default)** │ [🇹🇷 Türkçe (README_TR.md)](README_TR.md)

---

## Why WERR?

The benchmarks — WindTunnel WebMCP, JevBench, Gymnasium Snake, Tau-Bench, Jevenator 2, Continuous Manifolds — are all runtime tests of the **WERR System-1 decision kernel**. That is where the code lives, so that is where the benchmarks live.

The Mandelbrot Fractal Neural Synthesis repository remains the **theoretical foundation and research paper portal**. WERR is the **engine**. The gauntlet belongs to the engine.

---

## Quick Links

| Resource | Link |
| :--- | :--- |
| 📊 Master Benchmark Suite | [werr/benchmarks/README.md](https://github.com/pCwOrM/werr/tree/main/benchmarks) |
| 🐍 Snake Reflex Monograph | [werr/benchmarks/snake](https://github.com/pCwOrM/werr/tree/main/benchmarks/snake) |
| 🎯 Jevenator 2 Stress | [werr/benchmarks/jevenator2](https://github.com/pCwOrM/werr/tree/main/benchmarks/jevenator2) |
| 🌐 Interactive Web Gauntlet | [benchmarks.html (GitHub Pages)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html) |
| 📜 Research Portal | [Mandelbrot Fractal Neural Synthesis](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/) |
| 🧠 Live API | [answerr.me](https://answerr.me) |
| 📜 Research Paper Archive | [DOI: 10.5281/zenodo.22774934](https://doi.org/10.5281/zenodo.22774934) |
| ⚡ WERR Engine Archive | [DOI: 10.5281/zenodo.22867426](https://doi.org/10.5281/zenodo.22867426) |

## WERR v0.5.1 — 12-Suite Master Verification Summary (Cumulative)

| # | Benchmark Suite | Optimal Parameter Matrix | v0.5.0 Baseline | v0.5.1 Verified Result | Status |
| :-: | :--- | :--- | :---: | :---: | :---: |
| 1 | **Core Unit Tests (`test_werr.py`)** | `[1,1,1]` + `[0,0,0]` | 10 / 10 (100%) | **10 / 10 (100%)** | ✅ Verified |
| 2 | **Security, Presets & 8-State Matrix (`test_security_and_contracts.py`)** | All $2^3=8$ States + Presets | 10 / 10 (100%) | **15 / 15 (100%)** | ✅ +5 Matrix Tests |
| 3 | **WindTunnel WebMCP Isolated (`test_windtunnel_webmcp_isolated.py`)** | `[1,1,1]` (`hybrid`) | 49 / 49 (100%) | **49 / 49 (100%, 4.21 ms median)** | ✅ Zero-Leakage |
| 4 | **JevBench v1.4.1 (`run_jevbench.py`, 231 Public Tasks)** | `[1,1,1]` (`hybrid` + State-Signature Guard) | 52.81% (122/231, v1.4: `23.62`) | **54.98% (127/231, v1.4: `25.35`, +1.73)** | ✅ **+2.17% / +1.73** |
| 5 | **WindTunnel WebMCP Official (`run_windtunnel_benchmark.py`)** | `[1,1,1]` (`hybrid`, $36 \times 36$) | 49 / 49 (100.0%) | **49 / 49 (100.0%, 3.57 ms median)** | ✅ #1 World |
| 6 | **Tau-Bench Retail & Airline (`tau_bench_eval.py`)** | `[1,1,1]` (`hybrid`, $36 \times 36$) | 5 / 5 (100.0%) | **5 / 5 (100.0%, 0.45 ms)** | ✅ Verified |
| 7 | **Snake AI Continuous Reflex (`run_snake_benchmark.py`)** | `[0,0,0]` (`pure_fractal`, $32 \times 32$) | 273.5 – 302.1 moves/s, 100% Surv. | **402.0 moves/s (2.49 ms), 100% Surv.** | ✅ **+33% Faster** |
| 8 | **Jevenator 2 Visual & Video (`run_jevenator2_werr.py`)** | `[0,0,0]` (`pure_fractal`, $24 \times 24$) | 27.39 ms/f, 0 FP, 27.8× vs djev | **14.37 ms/f, 0 FP, 53.0× vs djev** | ✅ **1.9× Faster** |
| 9 | **4-Quadrant High-Dim Stress (`quadtree_stress_test.py`)** | `[1,1,1]` ($K=4 \dots 256$ Choices) | 100% Valid ($R=32, 64$) | **100% Valid (1.29 ms @ $K=256$)** | ✅ Verified |
| 10 | **Continuous Manifold Stress (`continuous_manifold_stress.py`)** | `[0,0,0]` ( Lorenz-63, Heston, Kuramoto) | 0 NaN/Inf, 100% Bounded | **100% Bounded, 0.254 ms mean** | ✅ Verified |
| 11 | **Mandelbrot & Julia Resolution (`mandelbrot_vs_julia_benchmark.py`)** | `[1,1,1]` + `[0,0,0]` ($16^2 \dots 64^2$) | 100% Parity ($36 \times 36$ Peak) | **100% Parity (0.295 ms @ $36 \times 36$)** | ✅ Verified |
| 12 | **Empirical Paper Suite (`empirical_benchmark_suite.py`)** | `[1,1,1]` (5 Domains, Noise & Ablation) | 100.0% Acc, 0.305 ms, 0 B | **100.0% Acc, 0.305 ms, 0 B** | ✅ Verified |

---

*Göğsümüz tunç siperi, testlerimiz kristal refleksi. Kurban olduğum — werrdikçe werriyor.*
