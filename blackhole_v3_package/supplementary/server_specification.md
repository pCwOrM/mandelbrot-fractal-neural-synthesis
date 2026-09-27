# Host specification for the exploratory run

Configuration of the bare-metal server on which the simulation was executed on 25 September 2026. Network addresses, open ports and security configuration are omitted from this public copy.

## Hardware

| Component | Specification |
| :--- | :--- |
| Motherboard | Supermicro X10DRL-i (dual socket, LGA 2011-3) |
| Processors | 2 × Intel Xeon E5-2630 v4 @ 2.20 GHz (Broadwell-EP, 14 nm) |
| Cores / threads | 20 physical cores / 40 logical threads (Hyper-Threading enabled) |
| Clock | Base 2.20 GHz, max all-core turbo 3.10 GHz; CPU governor fixed to `performance` |
| Instruction set extensions | AVX2, FMA3, BMI1, BMI2, AES-NI |
| Cache | L1d 32 KiB/core, L1i 32 KiB/core, L2 256 KiB/core, L3 25 MiB/socket (50 MiB total) |
| NUMA | 2 nodes (20 threads and ~128 GB each), QPI 8.0 GT/s |
| Memory | 256 GB DDR4 ECC Registered, quad-channel per socket |
| Storage | Samsung PCIe Gen4 NVMe 512 GB (OS, Python environment); 2 × Toshiba 2.7 TB SATA HDD (unused) |
| GPU | None used |

## Software

| Component | Version |
| :--- | :--- |
| Operating system | Ubuntu 24.04.5 LTS (x86_64) |
| Kernel | Linux 6.8.0-78-generic |
| Python | 3.12.3 |
| NumPy | 2.5.3 |

## Execution

The simulation script `simulate_blackhole_page_curve_40cores.py` was run with the Python 3.12.3 interpreter listed above, using 40 worker processes (`multiprocessing.Pool`). Its console output is provided in `run_console_log.txt`.
