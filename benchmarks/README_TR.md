# ⚔️ The Zero-VRAM Gauntlet — Kıyaslama Arşivi

> **📦 Bu dizin taşındı.**
>
> Tüm kıyaslama içeriği, test betikleri ve derinlemesine analizler artık **WERR deposunda** yaşıyor — zaten oraya ait:
>
> ## 👉 [github.com/pCwOrM/werr/tree/main/benchmarks](https://github.com/pCwOrM/werr/tree/main/benchmarks)

---

> 🌐 **Dil Seçici / Language Switcher:**  
> [🇬🇧 English (README.md)](README.md) │ **Türkçe (Aktif)**

---

## Neden WERR?

WindTunnel WebMCP, JevBench, Gymnasium Yılan, Tau-Bench, Jevenator 2, Sürekli Manifoldlar — bunların tamamı **WERR System-1 karar çekirdeğinin** çalışma zamanı testleri. Kod orada yaşıyor, kıyaslamalar da orada yaşıyor.

Mandelbrot Fraktal Sinir Sentezi deposu **teorik temel ve araştırma makalesi portalı** olmaya devam ediyor. WERR ise **motor**. Meydan okuma motora aittir.

---

## Hızlı Bağlantılar

| Kaynak | Bağlantı |
| :--- | :--- |
| 📊 Ana Kıyaslama Paketi | [werr/benchmarks/README.md](https://github.com/pCwOrM/werr/tree/main/benchmarks) |
| 🐍 Yılan Refleks Monografisi | [werr/benchmarks/snake](https://github.com/pCwOrM/werr/tree/main/benchmarks/snake) |
| 🎯 Jevenator 2 Stres Testi | [werr/benchmarks/jevenator2](https://github.com/pCwOrM/werr/tree/main/benchmarks/jevenator2) |
| 🌐 İnteraktif Web Arenası | [benchmarks.html (GitHub Pages)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html) |
| 📜 Araştırma Portalı | [Mandelbrot Fraktal Sinir Sentezi](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/) |
| 🧠 Canlı API | [answerr.me](https://answerr.me) |
| 📜 Araştırma Makalesi Arşivi | [DOI: 10.5281/zenodo.22774934](https://doi.org/10.5281/zenodo.22774934) |
| ⚡ WERR Motoru Arşivi | [DOI: 10.5281/zenodo.22867426](https://doi.org/10.5281/zenodo.22867426) |

## WERR v0.5.1 — 12 Paketlik Ana Doğrulama Özeti (Kümülatif)

| # | Kıyaslama Paketi | Optimal Parametre Matrisi | v0.5.0 Baz Çizgisi | v0.5.1 Doğrulanan Sonuç | Durum |
| :-: | :--- | :--- | :---: | :---: | :---: |
| 1 | **Çekirdek Birim Testleri (`test_werr.py`)** | `[1,1,1]` + `[0,0,0]` | 10 / 10 (%100) | **10 / 10 (%100)** | ✅ Doğrulandı |
| 2 | **Güvenlik, Hazır Profiller & 8-Durum Matrisi (`test_security_and_contracts.py`)** | Tüm $2^3=8$ Durum + Profiller | 10 / 10 (%100) | **15 / 15 (%100)** | ✅ +5 Matris Testi |
| 3 | **WindTunnel WebMCP İzole (`test_windtunnel_webmcp_isolated.py`)** | `[1,1,1]` (`hybrid`) | 49 / 49 (%100) | **49 / 49 (%100, 4.21 ms medyan)** | ✅ Sıfır Sızıntı |
| 4 | **JevBench v1.4.1 (`run_jevbench.py`, 231 Açık Görev)** | `[1,1,1]` (`hybrid` + Durum-İmzası Koruması) | %52.81 (122/231, v1.4: `23.62`) | **%54.98 (127/231, v1.4: `25.35`, +1.73)** | ✅ **+%2.17 / +1.73** |
| 5 | **WindTunnel WebMCP Resmî (`run_windtunnel_benchmark.py`)** | `[1,1,1]` (`hybrid`, $36 \times 36$) | 49 / 49 (%100.0) | **49 / 49 (%100.0, 3.57 ms medyan)** | ✅ Dünya #1 |
| 6 | **Tau-Bench Perakende & Havayolu (`tau_bench_eval.py`)** | `[1,1,1]` (`hybrid`, $36 \times 36$) | 5 / 5 (%100.0) | **5 / 5 (%100.0, 0.45 ms)** | ✅ Doğrulandı |
| 7 | **Snake AI Sürekli Refleks (`run_snake_benchmark.py`)** | `[0,0,0]` (`pure_fractal`, $32 \times 32$) | 273.5 – 302.1 hamle/s, %100 Sağkalım | **402.0 hamle/s (2.49 ms), %100 Sağkalım** | ✅ **+%33 Daha Hızlı** |
| 8 | **Jevenator 2 Görsel & Video (`run_jevenator2_werr.py`)** | `[0,0,0]` (`pure_fractal`, $24 \times 24$) | 27.39 ms/k, 0 FP, 27.8× vs djev | **14.37 ms/k, 0 FP, 53.0× vs djev** | ✅ **1.9× Daha Hızlı** |
| 9 | **4-Çeyrek Yüksek Boyutlu Stres (`quadtree_stress_test.py`)** | `[1,1,1]` ($K=4 \dots 256$ Seçenek) | %100 Geçerli ($R=32, 64$) | **%100 Geçerli (1.29 ms @ $K=256$)** | ✅ Doğrulandı |
| 10 | **Sürekli Manifold Stresi (`continuous_manifold_stress.py`)** | `[0,0,0]` (Lorenz-63, Heston, Kuramoto) | 0 NaN/Inf, %100 Sınırlı | **%100 Sınırlı, 0.254 ms ort.** | ✅ Doğrulandı |
| 11 | **Mandelbrot & Julia Çözünürlük (`mandelbrot_vs_julia_benchmark.py`)** | `[1,1,1]` + `[0,0,0]` ($16^2 \dots 64^2$) | %100 Eşlik ($36 \times 36$ Zirve) | **%100 Eşlik (0.295 ms @ $36 \times 36$)** | ✅ Doğrulandı |
| 12 | **Ampirik Makale Paketi (`empirical_benchmark_suite.py`)** | `[1,1,1]` (5 Alan, Gürültü & Ablasyon) | %100.0 Doğruluk, 0.305 ms, 0 B | **%100.0 Doğruluk, 0.305 ms, 0 B** | ✅ Doğrulandı |

---

*Göğsümüz tunç siperi, testlerimiz kristal refleksi. Kurban olduğum — werrdikçe werriyor.*
