"""
3-Arm Controlled Ablation Experiment: Classical vs. Phase 1 (Base Fractal) vs. Phase 3 (OED Injected)
Evaluated across 40 hardware CPU threads on 207.180.255.35 (Broadwell Dual Xeon, 256GB RAM).
"""
import time
import math
import multiprocessing as mp
import numpy as np

# -----------------------------------------------------------------------------
# Semi-Prime Generator
# -----------------------------------------------------------------------------
def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0: return False
        i += w
        w = 6 - w
    return True

def generate_semiprime(bits=48, seed=None):
    if seed is not None:
        np.random.seed(seed)
    half_bits = bits // 2
    low = 1 << (half_bits - 1)
    high = (1 << half_bits) - 1
    
    p = np.random.randint(low, high) | 1
    while not is_prime(p):
        p += 2
        
    q = np.random.randint(low, high) | 1
    while not is_prime(q) or q == p:
        q += 2
        
    return p * q, min(p, q), max(p, q)

# -----------------------------------------------------------------------------
# ARM 1: Classical Baseline (Brent's Cycle-Finding Algorithm)
# -----------------------------------------------------------------------------
def solve_arm1_classical(N, max_steps=500000):
    t0 = time.perf_counter()
    y = 2
    c = 1
    m = 128
    d = 1
    r = 1
    q = 1
    steps = 0
    
    while d == 1 and steps < max_steps:
        x = y
        for _ in range(r):
            y = (y * y + c) % N
            steps += 1
            
        k = 0
        while k < r and d == 1 and steps < max_steps:
            ys = y
            for _ in range(min(m, r - k)):
                y = (y * y + c) % N
                q = (q * abs(x - y)) % N
                steps += 1
            d = math.gcd(q, N)
            k += m
        r *= 2
        
    if d == N:
        while True:
            ys = (ys * ys + c) % N
            d = math.gcd(abs(x - ys), N)
            if d > 1:
                break
                
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    success = (1 < d < N)
    return {
        "arm": "Arm 1 (Classical Brent)",
        "success": success,
        "factor": d if success else None,
        "steps": steps,
        "time_ms": elapsed_ms
    }

# -----------------------------------------------------------------------------
# ARM 2: Phase 1 (Base Mandelbrot Fractal Core - No OED)
# Fixed complex seed (cx=-0.7436, cy=0.1318), single-track quadratic mapping
# -----------------------------------------------------------------------------
def solve_arm2_phase1(N, max_steps=500000):
    t0 = time.perf_counter()
    # Seahorse valley constant derived from cx, cy
    cx = -0.743643887
    cy = 0.131825904
    c_int = max(3, int(abs(cx * cy * 1000000)) % N | 1)
    
    y = int(abs(cx * 10000)) % N + 2
    m = 128
    d = 1
    r = 1
    q = 1
    steps = 0
    
    while d == 1 and steps < max_steps:
        x = y
        for _ in range(r):
            y = (y * y + c_int) % N
            steps += 1
            
        k = 0
        while k < r and d == 1 and steps < max_steps:
            ys = y
            for _ in range(min(m, r - k)):
                y = (y * y + c_int) % N
                q = (q * abs(x - y)) % N
                steps += 1
            d = math.gcd(q, N)
            k += m
        r *= 2
        
    if d == N:
        while True:
            ys = (ys * ys + c_int) % N
            d = math.gcd(abs(x - ys), N)
            if d > 1:
                break
                
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    success = (1 < d < N)
    return {
        "arm": "Arm 2 (Phase 1 Fractal Base)",
        "success": success,
        "factor": d if success else None,
        "steps": steps,
        "time_ms": elapsed_ms
    }

# -----------------------------------------------------------------------------
# ARM 3: Phase 3 (OED Injected: Cusp c=1/4 + Observer Horizon + Zinc Spark)
# -----------------------------------------------------------------------------
def solve_arm3_oed(N, max_steps=500000, stagnation_window=1000):
    t0 = time.perf_counter()
    
    # Observer Horizon: Cusp drag c = 1/4 (0.25) with twin shoulder resonance (±0.18)
    # Track A: X_upper (0.25 + 0.18)
    # Track B: X_lower (0.25 - 0.18)
    c_upper = max(3, int((0.25 + 0.18) * 10000) | 1)
    c_lower = max(3, int((0.25 - 0.18) * 10000) | 1)
    
    y_a = 2
    y_b = (2 + int(math.isqrt(N) * 0.18)) % N
    
    m = 64
    d = 1
    r = 1
    q = 1
    steps = 0
    sparks_count = 0
    stagnation_counter = 0
    
    while d == 1 and steps < max_steps:
        x_a = y_a
        x_b = y_b
        
        for _ in range(r):
            y_a = (y_a * y_a + c_upper) % N
            y_b = (y_b * y_b + c_lower) % N
            steps += 2
            stagnation_counter += 2
            
        k = 0
        while k < r and d == 1 and steps < max_steps:
            ys_a = y_a
            for _ in range(min(m, r - k)):
                y_a = (y_a * y_a + c_upper) % N
                y_b = (y_b * y_b + c_lower) % N
                
                # Check cross-horizon agreement
                q = (q * abs(y_a - y_b)) % N
                steps += 2
                stagnation_counter += 2
                
            d = math.gcd(q, N)
            k += m
            
            # Zinc Spark Quantum Tunneling Operator:
            # When trapped in non-converging orbits, apply heavy-tailed Cauchy kick
            if d == 1 and stagnation_counter >= stagnation_window:
                sparks_count += 1
                jump = int(np.random.standard_cauchy() * max(10, math.isqrt(N) * 0.05))
                y_a = (y_a + jump) % N
                y_b = (y_b - jump) % N
                stagnation_counter = 0
                
        r *= 2
        
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    success = (1 < d < N)
    return {
        "arm": "Arm 3 (Phase 3 OED Injected)",
        "success": success,
        "factor": d if success else None,
        "steps": steps,
        "time_ms": elapsed_ms,
        "sparks": sparks_count
    }

# -----------------------------------------------------------------------------
# Multi-Process Evaluation Task
# -----------------------------------------------------------------------------
def run_single_ablation_trial(args):
    case_idx, bits = args
    seed = case_idx * 1337 + 42
    N, p, q = generate_semiprime(bits=bits, seed=seed)
    
    res1 = solve_arm1_classical(N)
    res2 = solve_arm2_phase1(N)
    res3 = solve_arm3_oed(N)
    
    return {
        "case_idx": case_idx,
        "bits": bits,
        "N": N,
        "p": p,
        "q": q,
        "arm1": res1,
        "arm2": res2,
        "arm3": res3
    }

if __name__ == "__main__":
    print("=" * 85)
    print("  3-ARM ABLATION EXPERIMENT: CLASSICAL vs. PHASE 1 vs. PHASE 3 (OED)")
    print("  Empirical Evaluation on Production Dual Xeon Node (40 Cores / 256GB RAM)")
    print("=" * 85)
    
    num_cpus = mp.cpu_count()
    print(f"Hardware Worker Threads Active: {num_cpus}")
    
    test_scales = [40, 48, 56]
    trials_per_scale = 60
    
    summary_results = {}
    
    for bits in test_scales:
        print(f"\n" + "-" * 85)
        print(f"  RUNNING TEST SCALE: {bits}-BIT SEMI-PRIMES ({trials_per_scale} Monte Carlo Trials)...")
        print("-" * 85)
        
        args = [(i, bits) for i in range(trials_per_scale)]
        pool = mp.Pool(processes=num_cpus)
        t_start = time.perf_counter()
        results = pool.map(run_single_ablation_trial, args)
        pool.close()
        pool.join()
        total_time_scale = time.perf_counter() - t_start
        
        # Aggregate statistics
        succ1 = sum(1 for r in results if r["arm1"]["success"])
        succ2 = sum(1 for r in results if r["arm2"]["success"])
        succ3 = sum(1 for r in results if r["arm3"]["success"])
        
        steps1 = np.mean([r["arm1"]["steps"] for r in results if r["arm1"]["success"]]) if succ1 > 0 else 0
        steps2 = np.mean([r["arm2"]["steps"] for r in results if r["arm2"]["success"]]) if succ2 > 0 else 0
        steps3 = np.mean([r["arm3"]["steps"] for r in results if r["arm3"]["success"]]) if succ3 > 0 else 0
        
        time1 = np.mean([r["arm1"]["time_ms"] for r in results if r["arm1"]["success"]]) if succ1 > 0 else 0
        time2 = np.mean([r["arm2"]["time_ms"] for r in results if r["arm2"]["success"]]) if succ2 > 0 else 0
        time3 = np.mean([r["arm3"]["time_ms"] for r in results if r["arm3"]["success"]]) if succ3 > 0 else 0
        
        sparks3 = np.mean([r["arm3"].get("sparks", 0) for r in results])
        
        print(f"Results for {bits}-Bit Scale (Batch Completed in {total_time_scale:.2f}s):")
        print(f"  • Arm 1 (Classical Brent) : Success: {succ1}/{trials_per_scale} ({succ1/trials_per_scale*100:.1f}%) | Avg Steps: {steps1:,.1f} | Avg Latency: {time1:.2f} ms")
        print(f"  • Arm 2 (Phase 1 Fractal) : Success: {succ2}/{trials_per_scale} ({succ2/trials_per_scale*100:.1f}%) | Avg Steps: {steps2:,.1f} | Avg Latency: {time2:.2f} ms")
        print(f"  • Arm 3 (Phase 3 OED)     : Success: {succ3}/{trials_per_scale} ({succ3/trials_per_scale*100:.1f}%) | Avg Steps: {steps3:,.1f} | Avg Latency: {time3:.2f} ms (Sparks: {sparks3:.1f})")
        
        summary_results[bits] = {
            "arm1": {"success": succ1, "steps": steps1, "time_ms": time1},
            "arm2": {"success": succ2, "steps": steps2, "time_ms": time2},
            "arm3": {"success": succ3, "steps": steps3, "time_ms": time3},
        }

    print("\n" + "=" * 85)
    print("  3-ARM ABLATION EXPERIMENT COMPLETED WITH EMPIRICAL GROUND TRUTH!")
    print("=" * 85)
